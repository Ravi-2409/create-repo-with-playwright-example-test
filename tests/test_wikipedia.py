from playwright.sync_api import Playwright, sync_playwright, expect

def test_wikipedia_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://www.google.com/search?q=wikipedia&oq=wikipedia&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDQ0MzVqMGoyqAIAsAIA&sourceid=chrome&ie=UTF-8")
    page.get_by_role("heading", name="English", exact=True).click()
    page.get_by_role("heading", name="English", exact=True).click()
    page.get_by_role("link", name="Wikipedia Wikipedia https://www.wikipedia.org").click()
    page.get_by_label("Search Wikipedia").click()
    page.get_by_label("Search Wikipedia").fill("python")
    page.get_by_role("button", name="Search").click()
    expect(page.locator("#firstHeading")).to_contain_text("Python")
    expect(page.get_by_text("Look up Python or python in")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()