"""Minimal benchmark primitives for the Physics Truth Suite."""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt


STANDARD_GRAVITY = 9.80665


@dataclass(frozen=True)
class BenchmarkResult:
    """Result for a deterministic benchmark check."""

    experiment_id: str
    observed: float
    expected: float
    relative_error: float
    passed: bool


def relative_error(observed: float, expected: float) -> float:
    """Return relative error with a zero-safe exact-match branch."""

    if expected == 0:
        return 0.0 if observed == 0 else float("inf")
    return abs(observed - expected) / abs(expected)


def pendulum_small_angle_period(length_m: float, gravity_m_s2: float = STANDARD_GRAVITY) -> float:
    """Analytical small-angle pendulum period."""

    if length_m <= 0:
        raise ValueError("length_m must be positive")
    if gravity_m_s2 <= 0:
        raise ValueError("gravity_m_s2 must be positive")
    return 2 * pi * sqrt(length_m / gravity_m_s2)


def validate_pendulum_period(
    observed_period_s: float,
    length_m: float,
    tolerance: float = 0.01,
    gravity_m_s2: float = STANDARD_GRAVITY,
) -> BenchmarkResult:
    """Validate an observed pendulum period against the small-angle law."""

    expected = pendulum_small_angle_period(length_m, gravity_m_s2)
    error = relative_error(observed_period_s, expected)
    return BenchmarkResult(
        experiment_id="RK-MECH-001",
        observed=observed_period_s,
        expected=expected,
        relative_error=error,
        passed=error <= tolerance,
    )
