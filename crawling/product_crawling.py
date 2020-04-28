import time
import csv
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

csv_filename_to_write = 'unpacrwaling.csv'
csv_open = open(csv_filename_to_write, mode='w+', encoding=('utf-8'))
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('brand', 'product', 'product_image', 'like_number', 'review', 'mini', 'capacity', 'price'))

url = 'https://www.unpa.me/products'
driver = webdriver.Chrome('/home/soohyung/chromedriver')
driver.get(url)

first_category_path = driver.find_element_by_xpath('//*[@id="unpa-body"]/div[9]/div[1]')
first_categories = first_category_path.find_elements_by_class_name('category')

first_links = []
for first_category in first_categories[1:]:
    first_links.append(first_category.get_attribute('href'))

second_links = []
for first_link in first_links:
    driver.get(first_link)
    second_category_path = driver.find_element_by_xpath('//*[@id="unpa-body"]/div[9]/div[2]')
    second_categories = second_category_path.find_elements_by_class_name('category')

    for second_category in second_categories[1:]:
        second_links.append(second_category.get_attribute('href'))

for second_link in second_links:
    driver.get(second_link)
    # print(url)

    try:
        for i in range(1):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            driver.find_element_by_class_name('unpa-load-more-button').click()
            time.sleep(2)

        products = driver.find_elements_by_class_name('unpa-product')
        product_ids = []

        for product in products:
            product_ids.append(product.get_attribute('id'))

        for product_id in product_ids:
            ID = product_id
            url = f'https://www.unpa.me/product/detail/{ID}'
            driver.get(url)
            brand = driver.find_element_by_class_name('product-brand-name').text
            product = driver.find_element_by_class_name('product-name').text
            product_image_class = driver.find_element_by_class_name('product-main-image').get_attribute('style')
            product_image = re.compile("\((.*?)\)").findall(product_image_class)
            like_number = driver.find_element_by_css_selector('div.count-info > div.like-count > span').text
            review = driver.find_element_by_css_selector('div.count-info > div.power-review-count > span').text
            mini = driver.find_element_by_css_selector('div.count-info > div.mini-review-count > span').text
            capacity = driver.find_element_by_class_name('capacity').text
            price = driver.find_element_by_css_selector('div.col-sm-8 > div > div > div.value').text
            time.sleep(1)

            csv_writer.writerow((brand, product, product_image, like_number, review, mini, capacity, price))

    except NoSuchElementException:
        continue

    except ElementNotInteractableException:
        continue