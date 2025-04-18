"""
Unit tests for FTL calculations.
Run with pytest.
"""

import pytest
from controllers import ftl_calculator

def test_ftl_ok():
    schedule = {"crew": [{"id": 1, "duty_hours": 12}]}
    violations = ftl_calculator.check_ftl(schedule)
    assert violations == []

def test_ftl_violation():
    schedule = {"crew": [{"id": 2, "duty_hours": 16}]}
    violations = ftl_calculator.check_ftl(schedule)
    assert any("exceeds duty hours" in v for v in violations)
