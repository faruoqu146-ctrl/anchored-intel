# NexGene Intelligence Engine v0.1 Review Fix Build (v1.7.1)

## Phase 8: Genomic + Live Evidence Intelligence Foundation

v1.6.0 adds a Living Health Baseline and provenance-aware Evidence Fabric on top of the v1.5.0 genomic, live-evidence, live-context, and recurring-learning foundations.

### New layers

- **Genomic compartment**: separate database, opaque subject references, dual authorization, genomic variants, and polygenic scores with provenance.
- **Live evidence retrieval**: PubMed/NCBI E-utilities and Crossref metadata adapters.
- **Live context**: configurable weather/context retrieval based on user-configured city/country.
- **Recurring learning**: deterministic 90-day personal baseline cycle with model/version provenance.
- **Learning status**: `/api/v1/intelligence/learning/status` exposes recent learning artifacts for the authenticated user.

### Long-term intelligence direction

```text
Lifestyle + Physiological + Molecular + Clinical + Genetic
                         ↓
                 Data quality / provenance
                         ↓
                 Personal longitudinal models
                         ↓
             Live evidence + research retrieval
                         ↓
                  Evidence-weighted inference
                         ↓
                    Safety / escalation
                         ↓
                 Factual AI synthesis layer
```

The AI layer is downstream of structured evidence. It is not the source of truth and is not a substitute for clinical judgment.

### Development configuration

```bash
GENOMIC_DATABASE_URL=sqlite:///./nexgene_genomic.db
GENOMIC_PROVIDER_ID=development-genomics-provider
GENOMIC_PROVIDER_KEY=replace-with-a-local-development-secret
LIVE_CONTEXT_ENABLED=true
EVIDENCE_LIVE_ENABLED=true
NCBI_EMAIL=your-contact@example.com
NCBI_API_KEY=optional
CROSSREF_MAILTO=your-contact@example.com
```

NCBI requests should identify the application with tool/email and use an API key when higher supported request rates are needed. Crossref recommends a polite contact identity and caching/backoff for API use.

### Run

Production-safe defaults are now the Docker Compose defaults. Provide a strong secret explicitly:

```bash
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
docker compose up --build
```

For local development only, explicitly opt in to development mode:

```bash
DEV_MODE=true COOKIE_SECURE=false docker compose up --build
```

Recurring learning cycle, in a development environment:

```bash
python scripts/learning_cycle.py
```

A production deployment should schedule this worker rather than exposing it as an end-user action.

### Important boundaries

- No full genomic interpretation or clinical decision support is claimed by this release.
- Live evidence retrieval is metadata-first; it does not grant unrestricted rights to copyrighted full text.
- Live context is contextual information, not a diagnostic measurement.
- Clinical and genomic compartments remain separately authorized.
- The current mobile UI remains frozen while testing continues.

## Version

`APP_VERSION = 1.7.1`

`BUILD_VERSION = APP_VERSION`

`INTELLIGENCE_MODEL_VERSION = iei-0.1`

## Phase 9 / v1.6.0: Living Health Baseline + Evidence Fabric

NexGene no longer assumes that a person starts with a complete digital medical record. The pilot can begin with whatever reliable information exists today and progressively build a longitudinal profile.

Source progression:
`self-reported information -> documents -> lab data -> clinical records -> wearables/physiology -> genomic data -> molecular/biomarker data`

New foundations:
- user-owned source/provenance records for fragmented health information
- metadata-only document manifests for paper/PDF/lab/prescription records
- explicit observation-to-source provenance links
- `/api/v1/baseline/living` for longitudinal baseline stage and source-layer coverage
- persisted live-evidence snapshots with retrieval timestamp and content hash
- `/api/v1/evidence/snapshots` for the evidence cache
- versioned source-aware deterministic learning worker (`plb-1.1`)

Raw document storage and document OCR/extraction are intentionally not part of this phase. The pilot can test fragmented-source workflows without making file ingestion a prerequisite.


## Intelligence Engine v0.1 (build 1.7.0)

The next layer is now a structured, auditable scientific reasoning engine over personal longitudinal observations. It adds:

- first-class hypotheses with lifecycle/status
- competing explanations and explicit falsifiers
- daily temporal aggregation and lagged analysis
- Pearson association with Spearman sensitivity testing
- Fisher 95% confidence intervals
- Benjamini-Hochberg multiple-testing adjustment
- data-quality scoring
- derived longitudinal phenotypes
- forward, falsifiable predictions
- persistent hypothesis tests and scientific audit trails
- versioned intelligence runs

The engine remains observational. It does not establish causation, diagnosis, treatment, or population-level medical validity. The LLM layer remains downstream of structured analysis.

Run an authenticated development cycle with `POST /api/v1/intelligence/engine/run`. Inspect status at `GET /api/v1/intelligence/engine/status`.


## Intelligence Engine v0.1 review fixes

This build incorporates the first review hardening pass before additional intelligence layers are added.

- Student-t p-values for correlation tests, replacing the normal approximation.
- Calendar-day lag pairing, so missing dates never become artificial one-day lags.
- Prediction track records are persisted separately from the current statistical score. Repeated misses can weaken a hypothesis even when the latest correlation is strong.
- Prediction evaluation is conditioned on the stated exposure threshold and uses a trailing 14-day matched baseline. Unmet exposure conditions are inconclusive.
- Evidence snapshot query history is scoped to the authenticated user.
- BH correction is applied across all tested candidates before top-candidate selection.
- Daily buckets respect the user's configured timezone.
- A minimum active-week evidence gate prevents thin longitudinal evidence from being labelled supported.
- Numeric check-in kinds have finite-value and range validation.
- Intelligence-engine execution requires CSRF, rate limiting, and a per-user cooldown.
- Development mode is opt-in (`DEV_MODE=true`); production defaults are secure.
- Chunked request bodies are size checked. CSP reporting and HSTS are added for production.

The mobile/Raven UI remains frozen. This release is an analytical and infrastructure hardening build.
