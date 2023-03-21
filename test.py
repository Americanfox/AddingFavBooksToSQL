from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def launchbrowser():
    launch = True
    service = Service("D:\dev-tools\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(
        "https://en.wikipedia.org/wiki/Main_Page")
    # find_count = driver.find_element(By.ID, "articlecount")
    find_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
    print(find_count.text)
    # find_count.click() # Used to click something on screen ----------------------------------------

    # type_search = driver.find_element(By.LINK_TEXT, "Third Punic War")
    # type_search.click()

    search = driver.find_element(By.NAME, "search")
    search.send_keys("python") # Inserts text into something <----------------------------------
    search.send_keys(Keys.ENTER) # Must use and enter key using the import keys out of selenium

    while launch:
         pass

launchbrowser()