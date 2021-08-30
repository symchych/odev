from selenium.webdriver.common.by import By
from misc.setting import TestData
from pages.base_page import BasePage



class YoutubeMainPage(BasePage):

    '''BUTTONS'''
    SignInBtn = (By.CSS_SELECTOR, '[aria-label ="Sign in"]')
    loginBox = (By.ID, "identifierId")
    emailNextButton = (By.ID, "identifierNext")
    passWordBox = (By.XPATH, '//*[@id ="password"]/div[1]/div / div[1]/input')
    passwordNextButton = (By.ID, "passwordNext")
    usualUsersIcon = (By.XPATH, '//*[@alt="Avatar image" and @height="32"]')
    youChannelBtn = (By.XPATH, '//*[@id="label" and text()="Your channel"]')
    searchfield = (By.ID, 'search')
    seachbtn = (By.ID, 'search-icon-legacy')

    '''METHODS'''

    def __init__(self, driver):
        super().__init__(driver)

    def open_base_url(self):
        self.driver.get(TestData.base_url)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def does_signin_btn_exist(self):
        return self.is_element_visible(self.SignInBtn)

    def do_click_signin(self):
        try:
            self.do_click(self.SignInBtn)
        except:
            print("Cookies agreement window has shown. Trying with another sign in button...")
            self.do_click(self.SignInBtn)

    def do_login_email(self, username):
        self.do_send_keys(self.loginBox, username)
        self.do_click(self.emailNextButton)

    def do_login_password(self, password):
        self.do_send_keys(self.passWordBox, password)
        self.do_click(self.passwordNextButton)

    def verify_login_success(self):
        assert self.is_element_visible(self.usualUsersIcon), "user's icon not visible"

    def open_channel(self):
        self.do_click(self.usualUsersIcon)
        self.do_click(self.youChannelBtn)

    def enter_text_and_hit_search(self):
        self.do_send_keys(self.searchfield, TestData.search_for_a_video_data)
        self.do_click(self.seachbtn)









'''
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
from selenium.webdriver.common.keys import Keys
options.add_argument('--ignore-certificate-errors')
from misc import setting
'''
