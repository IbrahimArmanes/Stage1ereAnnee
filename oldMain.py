import requests
from selenium import webdriver
import urllib
import lxml
from bs4 import BeautifulSoup
"""
class EcoleScrapper(object):
    def __init__(self):
        self.
        self.driver.set_window_size(1120,550)
    def scrape_job_links(self):
        self.driver.get("https://www.ecoledirecte.com/login")
        
    def scrape(self):
        pass
Test = EcoleScrapper()
"""



#utiliser driver pour lire le JS et voir comment ouvrir une session en même temps

#Users/ibay4/Downloads/chromedriver_win32
with requests.Session() as s:
    driver = webdriver.Chrome(executable_path=r"C:/Users/ibay4/Downloads/chromedriver_win32/chromedriver.exe")
    url = "https://www.ecoledirecte.com/login"
    login_data = {'identifiant': "Armanes" , 'motdepasse': "Shurke15"}
    s.post(url, data=login_data)
    response = driver.get("https://www.ecoledirecte.com/login")


    #if response.ok:
    soup = BeautifulSoup(response.text,features="html.parser")
    title = soup.find("title")
    print(soup)