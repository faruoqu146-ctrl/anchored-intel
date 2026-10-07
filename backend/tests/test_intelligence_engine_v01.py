from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = (ROOT / "backend" / "app" / "main.py").read_text()
WORKER = (ROOT / "scripts" / "learning_cycle.py").read_text()

def test_intelligence_engine_v01_contract():
    assert 'BUILD_VERSION = "1.7.0-intelligence-v0.1"' in MAIN
    assert 'INTELLIGENCE_MODEL_VERSION = "iei-0.1"' in MAIN
    assert "class Hypothesis" in MAIN
    assert "class HypothesisTest" in MAIN
    assert "class Prediction" in MAIN
    assert "class PhenotypeDefinition" in MAIN
    assert "class PhenotypeObservation" in MAIN
    assert '/api/v1/intelligence/engine/run' in MAIN
    assert '/api/v1/intelligence/hypotheses' in MAIN
    assert '/api/v1/intelligence/predictions' in MAIN
    assert '/api/v1/intelligence/audit/{hypothesis_id}' in MAIN
    assert "Benjamini-Hochberg" in MAIN
    assert "Spearman" in MAIN
    assert "Fisher 95% CI" in MAIN

def test_existing_learning_worker_remains_compatible():
    assert 'MODEL_VERSION = "plb-1.1"' in WORKER
    assert 'source_aware' in WORKER
