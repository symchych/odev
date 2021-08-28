from misc.setting import TestData
from pages.youtube_main_page import YoutubeMainPage
from pages.youtube_channel_page import YoutubeChannelPage
from pages.youtube_video_page import YoutubeVideoPage
from jobs.test_base import BaseTest

class Test_Login(BaseTest):



    '''
    Test case:
    0. Log in
    1. Go to the uploaded videos (youtube studio)
    2. Open an uploaded video
    3. Comment it
    pytest jobs/test_comment_your_video.py
    $x('//*[@id="contenteditable-root" and @aria-label="Add a public comment..."]'
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

    #1. Go to the uploaded videos (youtube studio)
    def test_go_to_your_channel(self):
        self.youtube_main_page = YoutubeMainPage(self.driver)
        self.youtube_channel_page = YoutubeChannelPage(self.driver)
        self.youtube_main_page.open_base_url()
        self.youtube_main_page.open_channel()


    #2. Open an uploaded video
    def test_open_the_video(self):
        #self.youtube_main_page = YoutubeMainPage(self.driver)   #TEST
        self.youtube_channel_page = YoutubeChannelPage(self.driver)

        self.youtube_channel_page.open_video()
        #self.youtube_main_page.driver.maximize_window() #TEST
        #self.youtube_channel_page.open_video(TestData.youtube_link)
        #self.youtube_channel_page.sleep(300)

    #3. Comment opened video
    def test_comment(self):
        self.youtube_channel_page = YoutubeChannelPage(self.driver)
        self.youtube_video_page = YoutubeVideoPage(self.driver)
        self.youtube_video_page.scrolldown()
        self.youtube_video_page.do_comment(TestData.comment_text)
        self.youtube_video_page.check_that_comment_is_present()
        #self.youtube_channel_page.sleep(300)
















''' 
    Test methods
    def test_login_page_title(self):
        self.youtube_main_page = YoutubeMainPage(self.driver)
        title = self.youtube_main_page.get_title(TestData.youtube_main_page_title)
        assert title == TestData.youtube_main_page_title, "The title is wrong!"

    def test_signin_button_visible(self):
        self.youtube_main_page = YoutubeMainPage(self.driver)
        assert self.youtube_main_page.does_signin_btn_exist(), "The sign-in button doesn't exist!"
        '''

