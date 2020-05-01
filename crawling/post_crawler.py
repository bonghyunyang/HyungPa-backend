from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time
import requests
import re
import csv

url = ‘https://www.unpa.me/edit-content’
driver = webdriver.Chrome(‘/usr/local/bin/chromedriver’)
driver.get(url)
time.sleep(1)

for i in range(0,1):
    driver.find_element_by_class_name(‘unpa-load-more-button’).click()
    time.sleep(1)

products = driver.find_elements_by_class_name(‘unpa-card’)
product_ids = []

for product in products:
    product_ids.append(product.get_attribute(‘id’))

for product_id in product_ids:
    try:
        ID = product_id
        url = f’https://www.unpa.me/tip/detail/{ID}’
        driver.get(url)
        brand = driver.find_element_by_class_name(‘unpa-tip-detail-header’).text
        description = driver.find_element_by_xpath(‘//*[@id=“ID”]/div/div[2]/div[1]/div[1]/div[2]‘)
        like_number = driver.find_element_by_xpath(‘//*[@id=“ID”]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/a/div[2]‘)
        review = driver.find_element_by_xpath(‘//*[@id=“ID”]/div/div[2]/div[1]/div[2]/div[4]/div[2]/div[1]/div[2]’)
        time.sleep(2)
    except NoSuchElementException:
       continue
