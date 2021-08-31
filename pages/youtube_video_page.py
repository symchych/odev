from selenium.webdriver.common.by import By
from misc.setting import TestData
from pages.base_page import BasePage

class YoutubeVideoPage(BasePage):

    '''Variables'''

    mediaPlayer = (By.XPATH, '//*[@id="movie_player"]')
    searchfield = (By.ID, 'search')
    commentBox = (By.XPATH, '//*[@id="contenteditable-root" and @aria-label="Add a public comment..."]')
    commentButton = (By.CSS_SELECTOR, '[aria-label="Comment"]')
    commentBoxClickable = (By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer div#placeholder-area")
    commentElementCompleted = (By.XPATH, (('//*[@id="content-text" and text()="%s"]') % (TestData.comment_text)))
    hello = (By.XPATH, '//ytd-compact-video-renderer[%s]/div/ytd-thumbnail')
    videoTitle = (By.XPATH, '//ytd-video-primary-info-renderer[1]/div[1]/h1[1]/yt-formatted-string[1]')
    readyVideoTitleRecommendation = ""
    videoTiitle = (By.CSS_SELECTOR, "yt-formatted-string[class='style-scope ytd-video-primary-info-renderer']")
    list_of_recommended_videos = (By.CSS_SELECTOR, 'span[id="video-title"][class="style-scope ytd-compact-video-renderer"]')
    internalTitle = (By.XPATH, "/html[1]/body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]/div[5]/div[1]/div[1]/div[8]/div[2]/ytd-video-primary-info-renderer[1]/div[1]/h1[1]/yt-formatted-string[1]")
    likebutton = (By.XPATH, "//body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]/div[5]/div[1]/div[1]/div[6]/div[2]/ytd-video-primary-info-renderer[1]/div[1]/div[1]/div[3]/div[1]/ytd-menu-renderer[1]/div[1]/ytd-toggle-button-renderer[1]/a[1]/yt-icon-button[1]/button[1]")
    # because css is impossible yt-formatted-string[class='style-scope ytd-video-primary-info-renderer']
    ogorchenie = (By.XPATH, "//ytd-compact-video-renderer[%s]/div/ytd-thumbnail")


    '''METHODS'''

    def __init__(self, driver):
        super().__init__(driver)

    def check_media_player_visible(self):
        assert self.is_element_visible(self.mediaPlayer), "The media player is not visible!"

    def scrolldown(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")

    def scrollup(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def do_comment(self, comment):
        self.do_click(self.commentBoxClickable)
        self.driver.implicitly_wait(5)
        self.do_send_keys(self.commentBox, comment)
        self.do_click(self.commentButton)

    def check_that_comment_is_present(self):
        assert self.is_element_visible(self.commentElementCompleted), "The comment is wrong or doesn't exist!"

    def click_needed_recommendation(self, number):
        self.is_element_visible(self.mediaPlayer)
        self.sleep(1)
        array = self.find_elements(self.list_of_recommended_videos)
        externaltitle = array[number]
        self.do_click(self.searchfield)
        self.do_send_keys(self.searchfield, "asdasd")
        self.do_send_keys(self.searchfield, externaltitle)
        self.do_send_keys(self.searchfield, array)
        self.do_send_keys(self.searchfield, "asdasd")
        self.sleep(200)
        #self.do_click(array[number])
        #self.is_element_visible(self.internalTitle)
        #internaltitletext = self.get_element_text(self.internalTitle)
        #assert externaltitle == internaltitletext, "names doesn't match!"

    def original_click_recommendation(self, number):
        #self.sleep(2)
        self.do_click((By.XPATH, ("//ytd-compact-video-renderer[%s]/div/ytd-thumbnail") % (number)))
        #self.sleep(15)
        assert self.is_element_visible(self.mediaPlayer)
        self.sleep(5)

    def hit_like(self):
        self.is_element_visible(self.likebutton)
        self.do_click(self.likebutton)
        self.sleep(200)
















