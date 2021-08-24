import pytest
from selenium import webdriver
from misc.setting import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE)
    request.cls.driver = web_driver
    yield
    web_driver.close()