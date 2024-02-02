from playwright.sync_api import Playwright, sync_playwright, expect
class login_page():

    def __int__(self, page):
        self.base_url = "https://kindstaging.azure.dynamicdemand.ai/"
        self.login_page_text1 = page.get_by_text("Welcome to the")
        self.login_page_text2 = page.get_by_text("SRM Analytic Intelligence (AI")
        self.Email_placeholder = page.get_by_placeholder("Enter your Email ID")
        self.Email_email = page.get_by_placeholder("Enter your Email ID").fill("raviranjan.singh@asper.ai")
        self.Password_placeholder = page.get_by_placeholder("Enter your Password")
        self.Enter_password = page.get_by_placeholder("Enter your Password").fill("Mumbai#1234$")
        self.Forget_password = page.get_by_text("Forgot password?").click()
        self.Forget_password_details = page.get_by_placeholder("Enter your Email", exact=True)
        self.Forget_password_test = page.get_by_role("button", name="Send Reset Link")
        self.Login_btn = page.get_by_role("button", name="LOGIN").click()
        self.Landing_page = page.goto("https://kindstaging.azure.dynamicdemand.ai/promo/category-diagnostics/growth-analysis")


