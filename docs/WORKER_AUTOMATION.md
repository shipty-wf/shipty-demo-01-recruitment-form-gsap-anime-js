# Headed Browser Capture on shp-worker-01

This suite executes a visible, non-headless Playwright session on `shp-worker-01` to allow visual observation of browser navigation, live screenshot taking, and full-session video recording.

### Running on Worker Machine
```bash
chmod +x scripts/run_worker.sh
./scripts/run_worker.sh
```

### Execution Details
- **Target**: `https://webtactics.org/`
- **Mode**: `headless=False` with 1500ms `slow_mo` for live viewing
- **Video Artifact**: Captured to `artifacts/videos/`
- **Screenshot Artifact**: Captured to `artifacts/screenshots/webtactics_live_action.png`
- **DOM Snapshot**: Stored at `artifacts/webtactics_live.html`
