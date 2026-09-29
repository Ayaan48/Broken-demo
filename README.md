# Inventory Service (demo)

A tiny inventory service used to demo the Autonomous CI/CD Healing Agent.

**This repository is intentionally broken.** CI fails on it. Point the healing
agent at this repo and watch it detect, repair, and validate every defect.

Planted defects (all repairable without an AI model):

| File | Defect |
| --- | --- |
| `inventory/store.py` | mixed tabs/spaces indentation (two helpers use tabs), `== None` comparisons, unused import |
| `inventory/pricing.py` | `import os, sys` on one line, unsorted imports, trailing whitespace, `not x in y` |
| `inventory/report.py` | unused imports, blank-line whitespace, missing final newline |
| `config/settings.json` | trailing commas - invalid JSON, the app cannot load its config |

CI (`.github/workflows/ci.yml`) runs lint, a config check, and the tests, so it fails on `main` until the agent's healing branch is merged.

Run locally:

```bash
python -m pytest
```
