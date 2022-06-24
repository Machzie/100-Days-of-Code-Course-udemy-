# Day 48 Project - Selenium Web Automater
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "http://orteil.dashnet.org/experiments/cookie/"

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)

cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")


def buy_item():
    items = driver.find_elements(by=By.CSS_SELECTOR, value="#store > div")
    for i in range(len(items)-1, -1, -1):
        if items[i].get_attribute('class') == "":
            print(f"{items[i].get_attribute('id')}")
            items[i].click()
            break


fivemin = time.time() + 300
fivesec = time.time() + 5

while time.time() < fivemin:

    cookie.click()

    if time.time() > fivesec:
        buy_item()
        fivesec += 5

driver.close()
