from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://kindstaging.azure.dynamicdemand.ai/promo/category-diagnostics/growth-analysis")
    page.goto("https://kindstaging.azure.dynamicdemand.ai/")
    page.get_by_placeholder("Enter your Email ID").click()
    page.get_by_placeholder("Enter your Email ID").fill("raviranjan.singh@asper.ai")
    page.get_by_placeholder("Enter your Password").click()
    page.get_by_placeholder("Enter your Password").fill("Mumbai#1234$")
    page.get_by_role("button", name="LOGIN").click()
    #page.goto("https://kindstaging.azure.dynamicdemand.ai/implicit/callback?code=ZeYlrtkMjTmRjbxrcNb6T3XS8dc2KY89yqTPQ7vdKrY&state=tpSjZz017kz7XLMaV5QOCl8SiLEKLQGuA4iUyw8WPeD4BXYEV2fVAdWwNnMxasRX")
    page.goto("https://kindstaging.azure.dynamicdemand.ai/promo/category-diagnostics/growth-analysis")
    page.wait_for_selector(page.get_by_text("Category Diagnostics"))
    expect(page.get_by_text("Category Diagnostics")).to_be_visible()
    expect(page.get_by_text("Pricing Analytics")).to_be_visible()
    expect(page.get_by_text("Promo Analytics")).to_be_visible()
    expect(page.get_by_text("Price & Promo Modeling")).to_be_visible()
    expect(page.get_by_role("link", name="User Manual")).to_be_visible()
    page.get_by_text("RS", exact=True).click()
    page.get_by_text("Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
