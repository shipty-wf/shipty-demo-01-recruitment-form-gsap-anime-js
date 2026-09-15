#!/usr/bin/env bash
set -euo pipefail

echo "=== [shp-worker-01] Starting Headed QA Runner ==="
# Export display for visible desktop or virtual display (VNC/X11)
export DISPLAY=${DISPLAY:-":0"}

pip install -q playwright
playwright install chromium

python3 scripts/capture_webtactics_live.py
