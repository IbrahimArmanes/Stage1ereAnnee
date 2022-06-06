from selenium import webdriver
from getpass import getpass
import time

driver =  webdriver.Chrome(executable_path="C:\\Users\\ibay4\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get('https://www.brainyquote.com/')

research="life"

time.sleep(3)
button = driver. find_element_by_class_name('css-47sehv')
button.click()

research_textbox = driver.find_element_by_id('hmSearch')
research_textbox.send_keys(research)

search_button = driver.find_element_by_class_name('homeSearchButton')
search_button.submit()
time.sleep(3)

table_quote = driver.find_elements_by_id('qpos_1_1')
print(table_quote[0].text)