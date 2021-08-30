from misc.setting import TestData
from pages.youtube_main_page import YoutubeMainPage
from pages.youtube_channel_page import YoutubeChannelPage
from pages.youtube_video_page import YoutubeVideoPage
from pages.youtube_searched_videos_page import YoutubeSearchedVideosPage
from jobs.test_base import BaseTest

class Test_Search_and_like(BaseTest):

    '''
    Test case:
    1. Search a video and go inside.
    2. Open a video from recommendation (Select 6th item)
    pytest jobs/test_open_6th.py
    '''

    #0. Log in
    def test_login(self):
        self.youtube_main_page = YoutubeMainPage(self.driver)
        self.youtube_main_page.driver.maximize_window()
        self.youtube_main_page.open_base_url()
        self.youtube_main_page.do_click_signin()
        self.youtube_main_page.do_login_email(TestData.email)
        self.youtube_main_page.do_login_password(TestData.password)
        self.youtube_main_page.verify_login_success()

    def test_search_the_video_and_click(self):
        self.youtube_searched_videos_page = YoutubeSearchedVideosPage(self.driver)
        self.youtube_main_page = YoutubeMainPage(self.driver)
        self.youtube_main_page.enter_text_and_hit_search()
        self.youtube_searched_videos_page.click_nth_search_video_item(2)

    def test_check_and_hit_like(self):
        self.youtube_video_page = YoutubeVideoPage(self.driver)
        self.youtube_video_page.hit_like()


