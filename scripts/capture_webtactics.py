import asyncio
from playwright.async_api import async_playwright

async def capture_webtactics():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()
        
        # Navigate and wait for network stability
        await page.goto("https://webtactics.org/", wait_until="networkidle", timeout=30000)
        
        # 1. Capture full-page screenshot
        await page.screenshot(path="artifacts/webtactics_screen.png", full_page=True)
        
        # 2. Extract DOM content as HTML
        html_content = await page.content()
        with open("artifacts/webtactics_page.html", "w", encoding="utf-8") as f:
            f.write(html_content)
            
        await browser.close()
        print("[Chika] Captured artifacts/webtactics_screen.png and artifacts/webtactics_page.html successfully.")

if __name__ == "__main__":
    asyncio.run(capture_webtactics())
