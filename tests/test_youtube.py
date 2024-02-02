import asyncio
from playwright.async_api import Playwright, async_playwright, expect
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=youtube&oq=youtube&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDE5OTFqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8")
    page.get_by_role("link", name="YouTube: Home YouTube https").click()
    page.get_by_placeholder("Search").fill("ben10")
    page.get_by_placeholder("Search").press("Enter")
    page.goto("https://www.youtube.com/watch?v=WTndDRiN3dk")
    page.locator("video").click()
    context.close()
    browser.close()

