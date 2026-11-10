"""Unit tests for limitation calculation logic."""

from datetime import date

import pytest

from case_schema import CaseFile, Issue, Slot
from domain_config import get_config
from limitation import (
    _add_years,
    _extract_period_years,
    _parse_date,
    compute_limitation,
    consumer_protection_deadline_info,
)


def test_add_years_normal():
    d = date(2023, 5, 10)
    assert _add_years(d, 3) == date(2026, 5, 10)


def test_add_years_leap_day():
    # Feb 29, 2024 + 1 year (2025 is not leap) -> March 1, 2025
    d = date(2024, 2, 29)
    assert _add_years(d, 1) == date(2025, 3, 1)
    # Feb 29, 2024 + 4 years (2028 is leap) -> Feb 29, 2028
    assert _add_years(d, 4) == date(2028, 2, 29)


def test_extract_period_years():
    assert _extract_period_years("Period of limitation: Three years.") == 3
    assert _extract_period_years("within two years from cause") == 2
    assert _extract_period_years("Period: 3 years.") == 3
    assert _extract_period_years("12 years for possession") == 12
    assert _extract_period_years("no period specified") is None


def test_parse_date_various_formats():
    assert _parse_date("2025-03-14") == date(2025, 3, 14)
    assert _parse_date("2025-03") == date(2025, 3, 1)
    assert _parse_date("2025") == date(2025, 1, 1)
    assert _parse_date("asked on 2026-01-15") == date(2026, 1, 15)
    assert _parse_date("invalid") is None
    assert _parse_date(None) is None


def test_compute_limitation_fallback_slot():
    cfg = get_config("security_deposit")
    case = CaseFile(
        case_id="lim-1",
        issue=Issue(primary="security_deposit"),
        slots={
            "demand_made": Slot(value="yes via phone", status="known"),  # Non-date
            "tenancy_end_date": Slot(value="2024-06-30", status="known"),  # Valid date
        },
    )
    res = compute_limitation(case, cfg, today=date(2026, 11, 10))
    assert res.computable is True
    assert res.start_date == date(2024, 6, 30)
    assert res.deadline == date(2027, 6, 30)
    assert res.period_years == 3


def test_consumer_protection_deadline():
    cpa = consumer_protection_deadline_info()
    assert cpa["basis"] == "consumer_protection_act"
    assert cpa["period_years"] == 2
    assert cpa["chunk_id"] == "IND-FED-CPA-2019-SEC-069"
