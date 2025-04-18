"""
Unit tests for rest requirements checking.
Run these tests with pytest.
"""

import pytest
from controllers import rest_requirements

def test_rest_ok():
    schedule = {"crew": [{"id": 1, "rest_hours": 12}]}
    violations = rest_requirements.check_rest(schedule)
    assert violations == []

def test_rest_violation():
    schedule = {"crew": [{"id": 2, "rest_hours": 6}]}
    violations = rest_requirements.check_rest(schedule)
    assert any("insufficient rest" in v for v in violations)
