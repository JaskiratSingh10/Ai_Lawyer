"""Transcript capture for scenario runs.

A transcript = the full turn-by-turn record: every user turn, every agent
reply, plus the internal case state after each turn (slots, risk, verdict,
question counts). Saved to `<scenario_id>.md`.
"""
from __future__ import annotations

import json
from datetime import date
from typing import Any

SYSTEM_NOTE = "Evaluation date anchor: 2026-11-10"


class Transcript:
    def __init__(self, scenario_id: str, title: str, state: str, language: str):
        self.scenario_id = scenario_id
        self.title = title
        self.state = state
        self.language = language
        self.turns: list[dict[str, Any]] = []
        self.final_case: dict[str, Any] = {}
        self.checks: dict[str, Any] = {}

    def add_turn(self, turn_index: int, user_message: str, reply_text: str,
                 verdict: str, asked_questions: list[str], missing: list[str],
                 severity: str | None, case_snapshot: dict[str, Any]) -> None:
        self.turns.append({
            "turn": turn_index,
            "user": user_message,
            "agent": reply_text,
            "verdict": verdict,
            "asked_questions": asked_questions,
            "missing_required": missing,
            "severity": severity,
            "case_snapshot": case_snapshot,
        })

    def finalize(self, case: Any, checks: dict[str, Any]) -> None:
        self.final_case = case.model_dump() if hasattr(case, "model_dump") else dict(case)
        self.checks = checks

    def save(self, path: str) -> None:
        domain_exp = self.final_case.get("explanation_fields", {})
        payload = {
            "scenario": {"id": self.scenario_id, "title": self.title,
                          "state": self.state, "language": self.language,
                          "expected_intake": {"verdict": "ready", "escalation_severity": "none"}},
            "system_note": SYSTEM_NOTE,
            "turns": self.turns,
            "domain_explanation": domain_exp,
            "final_case": self.final_case,
            "checks": self.checks,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False, default=str)

    def to_markdown(self) -> str:
        lines: list[str] = []
        lines.append(f"# Scenario {self.scenario_id}: {self.title}")
        lines.append("")
        lines.append(f"**Scenario id:** {self.scenario_id}")
        lines.append(f"**Category:** {self.title.split(' ')[0] if self.title else 'na'}")
        lines.append(f"**State:** {self.state} | **Language:** {self.language}")
        lines.append(f"**Evaluation date anchor:** 2026-11-10")
        lines.append("")
        lines.append("## Full transcript")
        lines.append("")
        for t in self.turns:
            lines.append(f"### Turn {t['turn']}")
            lines.append("")
            lines.append("**User:**")
            lines.append("")
            lines.append("```")
            lines.append(t["user"])
            lines.append("```")
            lines.append("")
            lines.append("**Agent:**")
            lines.append("")
            lines.append("```")
            lines.append(t["agent"])
            lines.append("```")
            lines.append("")
            lines.append("**Debug:**")
            lines.append(f"- verdict: {t['verdict']}")
            lines.append(f"- asked_questions: {t['asked_questions']}")
            lines.append(f"- missing_required: {t['missing_required']}")
            lines.append(f"- escalation severity: {t['severity']}")
            lines.append("")
            lines.append("**Case snapshot:**")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(t["case_snapshot"], indent=2, ensure_ascii=False, default=str))
            lines.append("```")
            lines.append("")
        lines.append("## Final case state")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(self.final_case, indent=2, ensure_ascii=False, default=str))
        lines.append("```")
        lines.append("")
        lines.append("## Scoring checks")
        lines.append("")
        for k, v in self.checks.items():
            lines.append(f"- **{k}**: {v}")
        return "\n".join(lines)
