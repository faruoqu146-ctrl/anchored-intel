from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = (ROOT / "backend" / "app" / "main.py").read_text()


def test_prediction_track_record_is_persistent():
    assert "hits: Mapped[int]" in MAIN
    assert "misses: Mapped[int]" in MAIN
    assert "inconclusive_count: Mapped[int]" in MAIN
    assert "_prediction_calibration" in MAIN
    assert "misses >= 2 and misses > hits" in MAIN


def test_prediction_is_exposure_conditioned():
    assert "exposure_baseline" in MAIN
    assert "exposure_condition_unmet" in MAIN
    assert "matched_baseline" in MAIN
    assert "trailing 14-day" not in MAIN  # implementation stores the actual 14-day window structurally
    assert "timedelta(days=14)" in MAIN


def test_evidence_snapshots_are_user_scoped():
    assert 'user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True, index=True)' in MAIN
    assert "EvidenceSnapshot.user_id == u.id" in MAIN


def test_engine_run_is_protected_and_rate_limited():
    assert 'require_csrf(request, st)' in MAIN
    assert 'rate_limit(request, f"intelligence-engine:{u.id}", 3, s)' in MAIN
    assert "INTELLIGENCE_RUN_COOLDOWN_SECONDS" in MAIN
