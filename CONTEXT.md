# Context — Private Face ID (Single-Serve)

## Goal
Ship a privacy-first face re-ID demo where **only a non-invertible template** leaves the device. The app shows pipeline internals and the **exact payload** that is sent.

## Constraints
- **Single codebase, single serve** (FastHTML app serves UI + APIs + static)
- **No raw pixels or float embeddings** transmitted beyond client
- **Cancelable template** (seeded RP + sign → 256-bit hex) planned
- **Low footprint**; client-first processing when feasible
- **3-day delivery** target for an end-to-end demo

## Tech Choices
- **FastHTML**: HTML-first, HTMX-driven interactions, FT tags.
- **MonsterUI**: Theme headers and styled primitives; no SPA frameworks.
- **Uvicorn**: ASGI server; `serve()` via FastHTML.
- **Python pip**: standard dependency management.
- **Docker**: container image for single-serve deployment.
- **Fastlite** (later): SQLite ORM for templates/config.

## Phased Plan (Minimal, Testable)
- **Phase 0 (this repo)**: Nav + layout + health; no ML.
- **Phase 1**: Capture & visualization panels (raw frame, bbox placeholder, aligned crop placeholder, 12×12 preview, “what leaves device” card).
- **Phase 2**: Client-side face detection + alignment (JS asset; still no server calls).
- **Phase 3**: Client-side embedding (ONNX) + cancelable template (RP+sign); show hex payload & JSON preview.
- **Phase 4**: Server endpoints `/api/enroll` and `/api/match`; SQLite via Fastlite; Hamming matcher.
- **Phase 5**: Robustness panel: compare two faces; sweep vs enrolled; simple hist table.
- **Phase 6**: Privacy UX; seed rotation (`/admin/seed`); live events/notifications.
- **Phase 7**: Calibration page: quick positives/negatives; suggest τ.

## API Sketch (Phase 4+)
- `POST /api/enroll {user_id, template_hex}` → 200
- `POST /api/match {template_hex}` → `{best_user_id, distance, pass}`

## Security & Privacy Notes (Design Targets)
- Templates are **non-invertible**; recon attempts should not exceed chance identity.
- Seed rotation invalidates templates; plan per-user salt in Phase 8.
- Client shows outbound payload; explicit labels mark local-only vs transmitted data.

## Deployment
- Local: `pip install -r requirements.txt && python -m app.main`
- Docker: build/run as in README.
