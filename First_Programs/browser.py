from selenium import webdriver
import os
print(os.path)
driver = webdriver.Chrome()
driver.get('https://app.powerbi.com')
#element = driver.find_element_by_css_selector('button.with-class#or-id')
#element.click()