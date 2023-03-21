from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def launchbrowser():
    launch = True
    service = Service("D:\dev-tools\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(
        "http://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(By.ID, "cookie")
    click_cookie = True
    while click_cookie:
        cookie.click()


    while launch:
         pass

launchbrowser()