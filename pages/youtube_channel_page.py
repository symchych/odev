from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class YoutubeChannelPage(BasePage):
    uploadedVideo = (By.XPATH, '//*[@id="video-title" and text()="Hello test video!"]')


    def __init__(self, driver):
        super().__init__(driver)

    def open_video(self):
        self.do_click(self.uploadedVideo)
        #self.driver.get(video)










