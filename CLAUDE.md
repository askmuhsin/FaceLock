# FastHTML + Monster UI Development with uv

Developing web applications using FastHTML framework with Monster UI components, managed by uv package manager.

**CRITICAL**: Always reference `llm_ctxt/fasthtml_llms-ctx.txt` and `llm_ctxt/monster_ui_llms-ctx-full.txt` for accurate API usage, patterns, and architectural decisions. These official context files contain authoritative guidance for proper implementation.

## Project Architectural Decisions

**Import Style**: We use explicit imports instead of wildcard imports (`from fasthtml.common import *`). This diverges from official FastHTML examples for better code clarity and explicit dependency tracking.