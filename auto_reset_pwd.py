#!/usr/bin/python3
# -*- coding: utf-8 -*-

from multiprocessing.dummy import current_process
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
import pathlib
import os
import json

# load account info
cur_path = pathlib.Path(__file__).parent.resolve()
account_json_path = os.path.join(cur_path, "account.json")
print(account_json_path)
with open(account_json_path, "r") as file:
    account_data = json.load(file)
print(account_data)

# service = ChromeService(executable_path = ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.get("https://jssnd.edu.cn/login.html")

# username_ele = driver.find_element(By.ID, "user")
# password_ele = driver.find_element(By.ID, "login_psd") 

# username_ele.send_keys("test")

# sleep(5)
# driver.quit()
