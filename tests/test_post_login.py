# import playwright
# from playwright.sync_api import Page, expect
# import pytest
# from playwright.sync_api import sync_playwright
#
#
# def test_example(page: Page) -> None:
#         browser = playwright.chromium.launch(executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",headless=False, args=["--disable-incognito", "--start-maximized"])
#         context = browser.new_context(
#             viewport={'width': 1920, 'height': 1080}
#         )
#         page.goto("https://promo-kind.azure.dynamicdemand.ai/")
#         page.get_by_placeholder("Enter your Email ID").click()
#         page.get_by_placeholder("Enter your Email ID").fill("raviranjan.singh@asper.ai")
#         page.get_by_placeholder("Enter your Password").click()
#         page.get_by_placeholder("Enter your Password").fill("Mumbai#1234$")
#         page.get_by_role("button", name="LOGIN").click()
#         page.goto("https://promo-kind.azure.dynamicdemand.ai/implicit/callback?code=whHve7n7YzoX2OBfcMcmW_8n8FfKuSJZdbrXa0Zzhxk&state=nzNIfvZrUhE4pPF55JDyYJ2dHLXbTNgXYBNWeARMiioVL2yegFw6sBptdLp2D0eG")
#         page.goto("https://promo-kind.azure.dynamicdemand.ai/promo/category-diagnostics/growth-analysis")
#         expect(page.get_by_text("PromoCategory")).to_be_visible()
#         page.get_by_text("RS", exact=True).click()
#         page.get_by_text("Logout").click()

from playwright.sync_api import sync_playwright

def test_example() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            args=["--disable-incognito", "--start-maximized"],
        executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
            headless=False,
        )
        page = browser.new_page(
             viewport={'width': 1920, 'height': 1080}
        )
        with sync_playwright() as p:
            browser = p.chromium.launch(args=['--start-maximized'], headless=False)
            page = browser.new_page(no_viewport=True)
            page.goto(url)

        page.goto("https://promo-kind.azure.dynamicdemand.ai/")
        page.fill("input[placeholder='Enter your Email ID']", "raviranjan.singh@asper.ai")
        page.fill("input[placeholder='Enter your Password']", "Mumbai#1234$")
        page.click("button[name='LOGIN']")
        page.wait_for_load_state("networkidle")
        page.goto("https://promo-kind.azure.dynamicdemand.ai/promo/category-diagnostics/growth-analysis")
        assert page.is_visible("text=PromoCategory")
        page.click("text=RS")
        page.click("text=Logout")
        browser.close()
