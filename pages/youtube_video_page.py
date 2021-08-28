from selenium.webdriver.common.by import By
from misc.setting import TestData
from pages.base_page import BasePage

class YoutubeVideoPage(BasePage):

    '''Variables'''

    mediaPlayer = (By.XPATH, '//*[@id="movie_player"]')
    commentBox = (By.XPATH, '//*[@id="contenteditable-root" and @aria-label="Add a public comment..."]')
    commentButton = (By.CSS_SELECTOR, '[aria-label="Comment"]')
    commentBoxClickable = (By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer div#placeholder-area")
    commentElementCompleted = (By.XPATH, (('//*[@id="content-text" and text()="%s"]') % (TestData.comment_text)))
    print(commentElementCompleted)

    '''METHODS'''

    def __init__(self, driver):
        super().__init__(driver)

    def scrolldown(self):
        assert self.is_element_visible(self.mediaPlayer), "The media player is not visible!"
        self.driver.execute_script("window.scrollTo(0, 1000);")

    def do_comment(self, comment):
        self.do_click(self.commentBoxClickable)
        self.driver.implicitly_wait(5)
        self.do_send_keys(self.commentBox, comment)
        self.do_click(self.commentButton)

    def check_that_comment_is_present(self):
        assert self.is_element_visible(self.commentElementCompleted), "The comment is wrong or doesn't exist!"