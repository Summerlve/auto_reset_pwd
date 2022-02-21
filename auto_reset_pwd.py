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
import urllib.request
import pytesseract
from PIL import Image, ImageFilter

"""
def clear_and_save_image(image):
    image = clear_image(image)
    image = image.convert("L") # 灰度处理
    save_path = os.path.join(cur_path, "clear_auth_img.jpg")
    image.save(save_path)
    return image

def clear_image(image):
    image = image.convert("RGB")
    width = image.size[0]
    height = image.size[1]
    noise_color = get_noise_color(image)
    for x in range(width):
        for y in range(height):
            if (x == 0 or y == 0 or x == width - 1 or y == height - 1 or image.getpixel((x, y)) == noise_color):
                image.putpixel((x, y), (255, 255, 255))
    return image

def get_noise_color(image):
    for y in range(1, image.size[1] - 1):
        (r, g, b) = image.getpixel((2, y))
        if r < 255 and g < 255 and b < 255:
            return (r, g, b)
"""

# load account info
cur_path = pathlib.Path(__file__).parent.resolve()
account_json_path = os.path.join(cur_path, "account.json")
with open(account_json_path, "r") as file:
    account_data = json.load(file)

# get account info
username = account_data.get("username")
password = account_data.get("password")

# create webdriver
service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://jssnd.edu.cn/login.html")

username_ele = driver.find_element(By.ID, "user")
password_ele = driver.find_element(By.ID, "login_psd") 
auth_img_ele = driver.find_element(By.ID, "auth_img")

# fill in account info
username_ele.send_keys(username)
password_ele.send_keys(password)

# download auth_img
auth_img_src = auth_img_ele.get_attribute("src")
auth_img_path = os.path.join(cur_path, "auth_img.jpg")
urllib.request.urlretrieve(auth_img_src, auth_img_path)

# auth img recog and fill in
# auth_img = Image.open(auth_img_path)
# result = pytesseract.image_to_string(auth_img)

sleep(8) # wait for type in auth code

# log in
login_in_btn_ele = driver.find_element(By.ID, "login_btn")
login_in_btn_ele.click()

# nav to stu page
driver.get("https://jssnd.edu.cn/cs/s/student")

# get stu json data
sleep(8) # wait for type in auth code
driver.quit()