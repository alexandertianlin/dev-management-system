# Development Governance System — Codex Integration

This repository provides automated development compliance, enforcement, and workflow management.
When a task references this system, follow these steps:

## Entry Points

1. `_DEVELOPMENT_PROCEDURE.md` — Master procedure and directory conventions
2. `_ENFORCEMENT.md` — Violation penalty rules (L1-L4)
3. `_AGENTS_INTEGRATION.md` — Startup checklist for every new task

## Quick Reference

```bash
# Scan all tasks for compliance
python scripts/enforce_check.py

# Full CI with auto-heal and pass@3
python scripts/enforce_check.py --pass-n 3 --heal
```

## Task Structure Convention

Each task directory under `tasks/<task-id>/` should follow:

```
tasks/<task-id>/
├── _TASK_SPEC.md
├── _common/
├── models/
├── vX.Y-feat-<feature>-<YYYYMMDD>/
│   ├── _VERSION_SPEC.md
│   ├── src/
│   ├── config/
│   ├── lib/
│   └── requirements/
```
