# FaceLock

**FaceLock** is a privacy-first face re-identification demo.  
It shows that you can match faces without ever sending recognizable images or embeddings outside your device.  

Like [SpotlightPro](https://github.com/askmuhsin/SpotlightPro), this is a focused, minimal product built to demonstrate a single sharp idea.

---

## Why FaceLock?
- **No photos leave your device** — only a non-invertible template is sent.  
- **Transparent pipeline** — see exactly what happens to your data, step by step.  
- **Minimal + fast** — built with FastHTML + MonsterUI, deployable in a single container.  

---

## Quickstart (Local)

```bash
pip install -r requirements.txt
python -m app.main
```

Open [http://localhost:8000](http://localhost:8000).

---

## Docker

```bash
docker build -t facelock .
docker run --rm -p 8000:8000 -e APP_SEED=dev-seed facelock
```

---

## Roadmap (Condensed)

* Phase 0: Scaffold, nav, context
* Phase 1: Capture & visuals (no ML)
* Phase 2: On-device face detection & alignment
* Phase 3: On-device embeddings + cancelable template (256-bit hex)
* Phase 4: Minimal server match (Hamming distance)
* Phase 5: Robustness demo panel
* Phase 6: Privacy UX, seed rotation
* Phase 7: Calibration page (threshold τ)

---

## Constraints

* **Single codebase, single serve** — FastHTML app serves UI, API, and static.
* **Non-invertible data** — raw pixels and embeddings never leave the device.
* **Cancelable template** — seeded RP + sign → 256-bit hex payload.
* **Low footprint** — feasible for edge devices; fast enough for live demos.

---

## Tech Stack

* **FastHTML** — HTML-first framework (Starlette + HTMX + FastTags).
* **MonsterUI** — Tailwind-based component library.
* **Uvicorn** — ASGI server.
* **Python pip** — dependency management.
* **Docker** — containerized single-serve deployment.
* **Fastlite (later phases)** — SQLite ORM for template storage.

---
