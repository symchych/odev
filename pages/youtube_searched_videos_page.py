from selenium.webdriver.common.by import By
from misc.setting import TestData
from pages.base_page import BasePage

class YoutubeSearchedVideosPage(BasePage):

    sixthvideoelement = (By.XPATH, "//*[@class='yt-simple-endpoint inline-block style-scope ytd-thumbnail'][position()=2]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_nth_search_video_item(self, number):
        readyxpath = ((By.XPATH, ('//ytd-video-renderer[%s]/div/ytd-thumbnail') % (number)))
        self.do_click(readyxpath)







