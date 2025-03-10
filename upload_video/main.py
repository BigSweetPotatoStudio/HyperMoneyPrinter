from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    # default_context = browser.contexts[0]
    # page = default_context.pages[0]
    page = browser.new_page()
    page.goto("https://www.google.com")
    
    print(page)