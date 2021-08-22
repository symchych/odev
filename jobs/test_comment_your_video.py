import pytest
from misc.setting import TestData
from pages.youtube_main_page import YoutubeMainPage
from jobs.test_base import BaseTest

class Test_Login(BaseTest):

    '''def test_signin_button_visible(self):
        self.youtube_main_page = YoutubeMainPage(self.driver)
        flag = self.youtube_main_page.does_signin_btn_exist()
        assert flag'''

    def test_login_page_title(self):
        self.youtube_main_page = YoutubeMainPage(self.driver)
        title = self.youtube_main_page.get_title(TestData.youtube_main_page_title)
        assert title == TestData.youtube_main_page_title
'''
Test case:
0. Log in
1. Go to the uploaded videos (youtube studio)
2. Open an uploaded video
3. Comment it
'''












'''
driver.get("https://youtube.com/")
driver.maximize_window()
#driver.find_element_by_class_name("yt-simple-endpoint style-scope ytd-button-renderer").click()
try:
    driver.find_element_by_xpath(
        "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[1]/div[2]/div[2]/ytd-button-renderer/a").click()
except:
    print("there is no pop up window, switching to normal")
    driver.find_element_by_xpath(
        "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button").click()


driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("panzerpanzer@bigmir.net")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div[1]/input").send_keys("InsiderPass")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()
'''
'''class TestCommentYourVideo():
    def test_comment_your_video(self):
        driver.YoutubeMainPage.signinbtn.click()
'''
