from misc.setting import TestData
from pages.youtube_main_page import YoutubeMainPage
from jobs.test_base import BaseTest

class Test_Login(BaseTest):

    '''
    Test case:
    0. Log in
    1. Go to the uploaded videos (youtube studio)
    2. Open an uploaded video
    3. Comment it
    '''

    #0. Log in
    def test_login(self):
        self.youtube_main_page = YoutubeMainPage(self.driver)
        self.youtube_main_page.do_click_signin()
        self.youtube_main_page.do_login_email(TestData.email)
        self.youtube_main_page.do_login_password(TestData.password)
        self.youtube_main_page.verify_login_success()

    #1. Go to the uploaded videos (youtube studio)
    '''def go_to_your_channel(self):
        self.youtube_main_page.open_base_url()
        self.'''



















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

'''
from time import sleep
import pytest
'''