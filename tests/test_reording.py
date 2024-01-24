from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=python&oq=python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDEwOTBqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8")
    expect(page.locator("#rso")).to_contain_text("Welcome to Python.org")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
