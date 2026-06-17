# Create date: 2021.08.31
# Author: Sunhr
# Keep BIT-Web online

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions, ChromeOptions


def loopLoad(username, passwd, browserChoice='firefox'):
    browser = None
    try:
        while True:
            if browserChoice == 'firefox':
                opts = FirefoxOptions()
                opts.add_argument("--headless")
                browser = webdriver.Firefox(options=opts)
            elif browserChoice == 'chrome':
                opts = ChromeOptions()
                opts.add_argument("--headless")
                browser = webdriver.Chrome(options=opts)

            time.sleep(1)
            try:
                browser.get('https://portal.nwafu.edu.cn/')
                time.sleep(1)
                try:
                    if browser.find_element(By.ID, "logout"):
                        print("Bit-Web still OK!")
                        browser.quit()
                        time.sleep(random.randint(3, 7))
                        continue
                except Exception:
                    browser.find_element(By.ID, "username").clear()
                    browser.find_element(By.ID, "password").clear()
                    browser.find_element(By.ID, "username").send_keys(username)
                    browser.find_element(By.ID, "password").send_keys(passwd)
                    browser.find_element(By.ID, "login-account").click()
                    time.sleep(2)
                    print("Bit-Web OK!")

            except Exception:
                browser.quit()
                print("Bit-Web Failed!")
                continue
    finally:
        if browser is not None:
            try:
                browser.quit()
            except Exception:
                pass


if __name__ == '__main__':
    browserDict = {1: 'firefox', 2: 'chrome'}
    browserIdx = input('Please choose your browser number ( 1 for Firefox; 2 for Chrome ):')
    username = input("Please input username: ")
    passwd = input("Please input passwd: ")

    loopLoad(username, passwd, browserDict[int(browserIdx)])
