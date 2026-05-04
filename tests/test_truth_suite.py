from math import isclose, pi, sqrt

import pytest

from reality_kernel.truth_suite import (
    STANDARD_GRAVITY,
    pendulum_small_angle_period,
    validate_pendulum_period,
)


def test_pendulum_small_angle_period_matches_formula() -> None:
    length_m = 1.0
    expected = 2 * pi * sqrt(length_m / STANDARD_GRAVITY)

    assert isclose(pendulum_small_angle_period(length_m), expected)


def test_validate_pendulum_period_accepts_within_tolerance() -> None:
    expected = pendulum_small_angle_period(1.0)

    result = validate_pendulum_period(expected * 1.005, 1.0, tolerance=0.01)

    assert result.experiment_id == "RK-MECH-001"
    assert result.passed
    assert result.relative_error <= 0.01


def test_pendulum_length_must_be_positive() -> None:
    with pytest.raises(ValueError):
        pendulum_small_angle_period(0)
