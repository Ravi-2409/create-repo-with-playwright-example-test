import pytest
from playwright.sync_api import sync_playwright
from pom.youtube_search import YouTubePage


@pytest.mark.asyncio
def test_search_youtube_video():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        youtube_page = YouTubePage(page)

        youtube_page.open()
        search_query = "Python tutorial"
        youtube_page.search_video(search_query)

        first_video_link = youtube_page.get_first_video_link()
        print("First video link:", first_video_link)

        browser.close()
