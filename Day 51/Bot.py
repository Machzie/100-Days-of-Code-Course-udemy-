from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import Day51_config


class InternetSpeedTwitterBot():
    def __init__(self):
        self.service = Service("C:\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.speedtest_url = "https://www.speedtest.net/"
        self.twitter_url = "https://twitter.com/home"
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(self.speedtest_url)

        time.sleep(1)

        accept_cookies = self.driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
        accept_cookies.click()

        time.sleep(2)

        start_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-text")
        start_button.click()

        time.sleep(40)

        down_speed = self.driver.find_element(by=By.CSS_SELECTOR, value=".download-speed")
        self.down = down_speed.text
        print(f"down: {self.down}")

        up_speed = self.driver.find_element(by=By.CSS_SELECTOR, value=".upload-speed")
        self.up = up_speed.text
        print(f"up: {self.up}")

        self.driver.close()

        return [self.down, self.up]

    def tweet_at_provider(self, down, up):
        self.driver.get(self.twitter_url)

        time.sleep(3)

        username_input = self.driver.find_element(by=By.NAME, value="text")
        username_input.send_keys(Day51_config.account)
        username_input.send_keys(Keys.ENTER)

        time.sleep(1)

        password_input = self.driver.find_element(by=By.NAME, value="password")
        password_input.send_keys(Day51_config.password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(1)

        accept_cookies = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span')
        accept_cookies.click()

        time.sleep(1)

        tweet = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"My download speed is: {down:.0f} mbps, compared to the promised {Day51_config.PROMISED_DOWN} mbps"
                        f"\nMy upload speed is: {up:.0f} mbps, compared to the promised {Day51_config.PROMISED_UP} mbps")

        time.sleep(60)

        self.driver.close()
