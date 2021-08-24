from selenium.webdriver.common.by import By
from misc.setting import TestData
from pages.base_page import BasePage



class YoutubeMainPage(BasePage):

    '''BUTTONS'''
    SignInBtn = (By.CSS_SELECTOR, '[aria-label ="Sign in"]')
    loginBox = (By.XPATH, '//*[@id ="identifierId"]')
    emailNextButton = (By.XPATH, '//*[@id ="identifierNext"]')
    passWordBox = (By.XPATH,
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passwordNextButton = (By.XPATH, '//*[@id ="passwordNext"]')
    usualUsersIcon = (By.XPATH, '//*[@alt="Avatar image" and @height="32"]')
    usersChannelBtn = (By.XPATH, '//*[@id="label" and ')

    '''METHODS'''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    '''def open_base_url(self):
        self.driver.get(TestData.base_url)'''

    def get_login_page_title(self, title):
        return self.get_title(title)

    def does_signin_btn_exist(self):
        return self.is_element_visible(self.SignInBtn)

    def do_click_signin(self):
        self.do_click(self.SignInBtn)

    def do_login_email(self, username):
        self.do_send_keys(self.loginBox, username)
        self.do_click(self.emailNextButton)

    def do_login_password(self, password):
        self.do_send_keys(self.passWordBox, password)
        self.do_click(self.passwordNextButton)

    def verify_login_success(self):
        assert self.is_element_visible(self.usualUsersIcon), "user's icon not visible"

    '''def open_channel(self):
        self.do_click(self.usualUsersIcon)
        self.do_click()
'''






'''
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
from selenium.webdriver.common.keys import Keys
options.add_argument('--ignore-certificate-errors')
from misc import setting
'''
