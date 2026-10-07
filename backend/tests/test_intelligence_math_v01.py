from datetime import timedelta

from backend.app.main import (
    _lag_pairs,
    _normal_p_from_r,
)


def test_student_t_p_values_match_reference_values():
    assert abs(_normal_p_from_r(0.5, 8) - 0.20703125) < 1e-6
    assert abs(_normal_p_from_r(0.5, 10) - 0.14111328125) < 1e-6
    assert abs(_normal_p_from_r(0.4, 30) - 0.02851305940446) < 1e-6


def test_calendar_lag_does_not_cross_missing_days():
    daily = {
        "2026-01-02": {"sleep_duration": 5.0},
        "2026-01-10": {"focus": 2.0},
    }
    xs, ys, dates = _lag_pairs(daily, "sleep_duration", "focus", 1)
    assert xs == []
    assert ys == []
    assert dates == []


def test_calendar_lag_pairs_actual_next_day():
    daily = {
        "2026-01-02": {"sleep_duration": 5.0},
        "2026-01-03": {"focus": 2.0},
    }
    xs, ys, dates = _lag_pairs(daily, "sleep_duration", "focus", 1)
    assert xs == [5.0]
    assert ys == [2.0]
    assert dates == [("2026-01-02", "2026-01-03")]
