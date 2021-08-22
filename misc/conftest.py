import pytest
from selenium import webdriver
from misc.setting import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE)
    if request.param == "firefox":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE)
    request.cls.driver = web_driver
    yield
    web_driver.close()