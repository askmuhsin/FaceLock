from __future__ import annotations

import os
from typing import Any, Iterable

try:
    # FastHTML core
    from fasthtml.common import (
        fast_app, serve, Titled, Div, P, H1, H2, Ul, Li, A, Strong, Code, Pre,
        HtmxResponseHeaders, cookie, Script, Safe, Container as FTContainer
    )
except Exception as e:  # pragma: no cover
    raise SystemExit("FastHTML is required: pip/uv install fasthtml") from e

# MonsterUI theme headers (optional in Phase 0)
try:
    from monsterui import Theme
    _headers = [Theme.blue.headers(highlightjs=True)]
except Exception:
    _headers = []

APP_NAME = os.getenv("APP_NAME", "Private Face ID")
APP_SEED = os.getenv("APP_SEED", "dev-seed")
PORT = int(os.getenv("PORT", "8000"))

app, rt = fast_app(hdrs=_headers)

def _nav() -> Any:
    return Div(
        A("Home", href="/", cls="mr-4 link"),
        A("Enroll", href="/enroll", cls="mr-4 link"),
        A("Match", href="/match", cls="mr-4 link"),
        A("Admin · Seed", href="/admin/seed", cls="mr-4 link"),
        A("Health", href="/health", cls="mr-4 link"),
        cls="p-4 border-b border-base-300 flex gap-4"
    )

def _container(*children: Any) -> Any:
    return Div(*children, cls="max-w-5xl mx-auto p-4")

@rt
def index() -> Any:
    return Titled(
        APP_NAME,
        _nav(),
        _container(
            H1(APP_NAME),
            P("Phase 0 scaffold; navigation only."),
            H2("What you'll see next"),
            Ul(
                Li("Capture & visuals (no ML)"),
                Li("On-device detection/alignment"),
                Li("On-device embedding + 256-bit template (hex only leaves device)"),
                Li("Minimal enroll/match server with Hamming threshold"),
            ),
            P("See ", A("CONTEXT", href="/context", cls="link"), " for plan & constraints."),
        ),
    )

@rt
def enroll() -> Any:
    return Titled(
        f"{APP_NAME} · Enroll",
        _nav(),
        _container(
            H1("Enroll (Placeholder)"),
            P("Phase 1–4 will add capture and enroll UI here.")
        ),
    )

@rt
def match() -> Any:
    return Titled(
        f"{APP_NAME} · Match",
        _nav(),
        _container(
            H1("Match (Placeholder)"),
            P("Phase 1–4 will add capture and match UI here.")
        ),
    )

@rt
def admin_seed() -> Any:
    return Titled(
        f"{APP_NAME} · Admin · Seed",
        _nav(),
        _container(
            H1("Seed Rotation (Placeholder)"),
            P("Current seed: "), Code(APP_SEED),
            P("Phase 6 will enable rotation & template invalidation.")
        ),
    )

@rt
def context() -> Any:
    # Render CONTEXT.md as preformatted for now (MonsterUI markdown comes later)
    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "CONTEXT.md"), "r", encoding="utf-8") as f:
            md = f.read()
    except FileNotFoundError:
        md = "# CONTEXT.md not found"
    return Titled(
        f"{APP_NAME} · Context",
        _nav(),
        _container(
            H1("Context"),
            Pre(md, cls="whitespace-pre-wrap")
        ),
    )

@rt
def health() -> dict[str, Any]:
    return {"ok": True, "app": APP_NAME, "seed": APP_SEED}

def serve_app() -> None:
    serve()
