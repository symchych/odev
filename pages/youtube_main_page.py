from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument('--ignore-certificate-errors')
from misc import setting
from misc.setting import TestData
from pages.base_page import BasePage

class YoutubeMainPage(BasePage):
    '''BUTTONS'''
    signinbtn = (By.CSS_SELECTOR, '[aria-label ="Sign in"]')
    loginBox = (By.XPATH, '//*[@id ="identifierId"]')
    emailNextButton = (By.XPATH, '//*[@id ="identifierNext"]')
    passWordBox = (By.XPATH,
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passwordNextButton = (By.XPATH, '//*[@id ="passwordNext"]')
    usualusersicon = (By.XPATH, '//*[@alt="Avatar image", height="33"]')

    '''METHODS'''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def open_base_url(self):
        self.driver.get(TestData.base_url)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def does_signin_btn_exist(self):
        return self.is_element_visible(self.signinbtn)

    def do_click_signin(self):
        self.do_click(self.signinbtn)

    def do_login_email(self, username):
        self.do_send_keys(self.loginBox, username)
        self.do_click(self.emailNextButton)

    def do_login_password(self, password):
        self.do_send_keys(self.passWordBox, password)
        self.do_click(self.passwordNextButton)

    def verify_login_success(self):
        assert self.is_element_visible((By.XPATH, self.usualusersicon)), "user's icon not visible"





    '''test items'''
    def do_crazy(self):
        self.do_click(self.usualusersicon)


    #def is_login_window_visible(self, by_locator):


'''    def log_in(self, ):
        self.do_click(self.signinbtn)
'''







"""#try:
    YoutubeMainPage.driver.get("https://youtube.com/")
    YoutubeMainPage.driver.maximize_window()
    YoutubeMainPage.driver.signinbtn.click()

    YoutubeMainPage.driver.implicitly_wait(15)
    YoutubeMainPage.driver.loginBox.send_keys()
    YoutubeMainPage.driver.emailNextButton[0].click()
    YoutubeMainPage.driver.passWordBox.send_keys(setting.TestData.password)
    YoutubeMainPage.driver.passwordNextButton[0].click()
    print('Login Successful...!!')
except:
    print('Login Failed')

"""

'''
loginfield = driver.find_element_by_name("email")
loginfield.clear()


passwordfield = driver.find_element_by_name("password")
passwordfield.clear()


driver.find_element_by_id("login-button").click()
'''


#assert "No results found." not in driver.page_source
#driver.close()
#if __name__ == '__main__':

