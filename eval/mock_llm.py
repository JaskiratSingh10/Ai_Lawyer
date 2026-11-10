"""Deterministic LLM mock for offline scenario evaluation.

The scenario files encode per-scenario `must_do` / `must_not_do` clauses. This
mock maps those clauses onto a deterministic ``Extraction`` object (intake mode)
or a ``LLMExplanation`` object (explain mode) so the deterministic
readiness/escalation logic of ``intake_agent`` and ``domain_agent`` runs for
real and decides the verdict.
"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator


class _Risk(BaseModel):
    police_or_arrest: bool = False
    criminal_allegation_against_user: bool = False
    threats_or_violence: bool = False
    domestic_violence: bool = False
    court_summons_or_hearing_date: str | None = None
    notice_reply_deadline: str | None = None


class _Extraction(BaseModel):
    primary_issue: str = "other"
    issue_confidence: float = 0.9
    secondary_issues: list[str] = []
    state: str | None = None
    city: str | None = None
    user_role: str | None = None
    slot_fills: list[Any] = []
    parties: list[dict] = []
    timeline: list[dict] = []
    amounts: list[dict] = []
    evidence: list[dict] = []
    risk: _Risk = _Risk()
    notice_received: bool = False
    notice_sender: str | None = None
    notice_claims: str | None = None
    notice_demanded_amount: float | None = None
    notice_reply_deadline: str | None = None
    detected_language: str = "en"
    summary: str = ""


class _Option(BaseModel):
    title: str
    description: str
    next_steps: str
    chunk_ids: list[str] = Field(default_factory=list)
    supporting_quote: str = ""

    @field_validator("title", "description", "supporting_quote", mode="before")
    @classmethod
    def coerce_text(cls, v: Any) -> str:
        if isinstance(v, list):
            return " ".join(str(item).strip() for item in v if item)
        return str(v) if v is not None else ""

    @field_validator("next_steps", mode="before")
    @classmethod
    def coerce_next_steps(cls, v: Any) -> str:
        if isinstance(v, list):
            return "; ".join(str(item).strip() for item in v if item)
        return str(v) if v is not None else ""

    @field_validator("chunk_ids", mode="before")
    @classmethod
    def coerce_chunk_ids(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [c.strip() for c in re.split(r"[,;\s]+", v) if c.strip()]
        if isinstance(v, list):
            out = []
            for item in v:
                if isinstance(item, str):
                    out.append(item.strip())
                elif isinstance(item, dict):
                    cid = item.get("id") or item.get("chunk_id")
                    if cid:
                        out.append(str(cid).strip())
            return out
        return []


class _OtherSideArg(BaseModel):
    argument: str
    chunk_ids: list[str] = Field(default_factory=list)
    supporting_quote: str = ""

    @field_validator("argument", "supporting_quote", mode="before")
    @classmethod
    def coerce_text(cls, v: Any) -> str:
        if isinstance(v, list):
            return " ".join(str(item).strip() for item in v if item)
        return str(v) if v is not None else ""

    @field_validator("chunk_ids", mode="before")
    @classmethod
    def coerce_chunk_ids(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [c.strip() for c in re.split(r"[,;\s]+", v) if c.strip()]
        if isinstance(v, list):
            out = []
            for item in v:
                if isinstance(item, str):
                    out.append(item.strip())
                elif isinstance(item, dict):
                    cid = item.get("id") or item.get("chunk_id")
                    if cid:
                        out.append(str(cid).strip())
            return out
        return []


class _LLMExplanation(BaseModel):
    """LLMExplanation-shaped object for the domain (explain) agent."""
    summary: str = ""
    summary_chunk_ids: list[str] = Field(default_factory=list)
    summary_supporting_quote: str = ""
    options: list[_Option] = Field(default_factory=list)
    other_side: list[_OtherSideArg] = Field(default_factory=list)
    evidence_gaps: list[str] = Field(default_factory=list)
    uncertainties: list[str] = Field(default_factory=list)
    removed_claims: list[dict] = Field(default_factory=dict)


class _SlotFill:
    """Tiny object standing in for the intake pipeline's SlotFill model.

    The pipeline's ``merge_extraction`` accesses ``.key``, ``.value``, and
    (optionally) ``.status`` / ``.source``.
    """
    def __init__(self, key: str, value: Any, confidence: float = 1.0):
        self.key = key
        self.value = value
        self.confidence = confidence
        self.status = "known"
        self.source = "user"
        self.raw_quote = None

    def get(self, key: str, default: Any = None) -> Any:
        """Dict-like access for the mock's internal use."""
        return getattr(self, key, default)


class MockLLMClient:
    """Deterministic LLM client. ``mode`` selects the schema returned."""

    def __init__(
        self,
        scenario_id: str,
        turn_index: int,
        extraction: dict[str, Any] | None = None,
        mode: str = "intake",
    ):
        self.scenario_id = scenario_id
        self.turn_index = turn_index
        self._extraction = extraction or {}
        self.mode = mode

    def complete(self, prompt: str, schema: type[Any]) -> Any:
        data = {
            "primary_issue": self._extraction.get("primary_issue", "other"),
            "issue_confidence": self._extraction.get("issue_confidence", 0.9),
            "state": self._extraction.get("state", None),
            "city": self._extraction.get("city", None),
            "user_role": self._extraction.get("user_role", None),
            "detected_language": self._extraction.get("detected_language", "en"),
            "summary": self._extraction.get("summary", ""),
            "slot_fills": [
                _SlotFill(f.get("key", ""), f.get("value", ""), f.get("confidence", 1.0))
                for f in self._extraction.get("slot_fills", [])
            ],
            "amounts": self._extraction.get("amounts", []),
            "evidence": self._extraction.get("evidence", []),
            "timeline": self._extraction.get("timeline", []),
            "secondary_issues": self._extraction.get("secondary_issues", []),
            "notice_received": self._extraction.get("notice_received", False),
            "notice_sender": self._extraction.get("notice_sender", None),
            "notice_claims": self._extraction.get("notice_claims", None),
            "notice_demanded_amount": self._extraction.get("notice_demanded_amount", None),
            "notice_reply_deadline": self._extraction.get("notice_reply_deadline", None),
        }
        risk = self._extraction.get("risk", {})
        if isinstance(risk, dict):
            data["risk"] = {
                "police_or_arrest": bool(risk.get("police_or_arrest", False)),
                "criminal_allegation_against_user": bool(risk.get("criminal_allegation_against_user", False)),
                "threats_or_violence": bool(risk.get("threats_or_violence", False)),
                "domestic_violence": bool(risk.get("domestic_violence", False)),
                "court_summons_or_hearing_date": risk.get("court_summons_or_hearing_date", None),
                "notice_reply_deadline": risk.get("notice_reply_deadline", None),
            }
        if self.mode == "explain":
            return _LLMExplanation(**data)
        return _Extraction(**data)
