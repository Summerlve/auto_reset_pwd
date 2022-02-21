#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://jssnd.edu.cn/manager.html")
sleep(5)
driver.quit()
