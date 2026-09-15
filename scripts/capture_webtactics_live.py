import asyncio
import os
from playwright.async_api import async_playwright

async def run_live_capture():
    os.makedirs("artifacts/videos", exist_ok=True)
    os.makedirs("artifacts/screenshots", exist_ok=True)
    
    print("[Chika] Initializing Playwright headed browser session on shp-worker-01...")
    async with async_playwright() as p:
        # Launch visible browser with slow-motion to see live interactions
        browser = await p.chromium.launch(
            headless=False,
            slow_mo=1500,
            args=["--start-maximized"]
        )
        
        context = await browser.new_context(
            no_viewport=True,
            record_video_dir="artifacts/videos/",
            record_video_size={"width": 1920, "height": 1080}
        )
        
        page = await context.new_page()
        print("[Chika] Browser launched. Navigating to https://webtactics.org/...")
        
        await page.goto("https://webtactics.org/", wait_until="networkidle", timeout=45000)
        await page.wait_for_timeout(3000)
        
        print("[Chika] Taking screenshot in action...")
        await page.screenshot(path="artifacts/screenshots/webtactics_live_action.png", full_page=True)
        
        print("[Chika] Extracting DOM snapshot...")
        html_content = await page.content()
        with open("artifacts/webtactics_live.html", "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print("[Chika] Artifacts saved. Closing browser and finalizing video session...")
        await context.close()
        await browser.close()
        print("[Chika] Live session execution completed successfully.")

if __name__ == "__main__":
    asyncio.run(run_live_capture())
