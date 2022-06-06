
from selenium import webdriver
from getpass import getpass
import time

driver =  webdriver.Chrome(executable_path="C:\\Users\\ibay4\\Downloads\\chromedriver_win32\\chromedriver.exe")



accept = input("Envoyer le fichier contenant les notes par mail ? (y/n)")


while accept != 'y' and accept != 'n':
    accept = input("Veuillez entrer \"y\" pour envoyer par mail ou bien \"n\" pour ne pas envoyer")

if accept == 'y':

    mailLogin = input ("Entrez votre mail")
    mailPass = getpass("Entrez votre mot de passe de mail")
    mailDestinataire = input("Entrez l'adresse mail du destinataire")
     
    driver.get('https://login.live.com/login.srf')
    time.sleep(3)
    mailBox = driver.find_element_by_id('i0116')
    mailBox.send_keys(mailLogin)

    nextButton = driver.find_element_by_id('idSIButton9')
    nextButton.click()
    time.sleep(1)

    passBox = driver.find_element_by_id('i0118')
    passBox.send_keys(mailPass)
    nextButton.click()
    time.sleep(1)

    nextButton = driver.find_element_by_xpath('//*[@id="O365_MainLink_NavMenu"]/span')
    nextButton.click()
    time.sleep(1)
    nextButton = driver.find_element_by_xpath('//*[@id="O365_AppTile_Mail"]/div[2]/span')
    nextButton.click()
    time.sleep(1)
    nextButton = driver.find_element_by_xpath('//*[@id="iLooksGood"]')
    nextButton.click()
    time.sleep(5)
    nextButton = driver.find_element_by_xpath('//*[@id="id__7"]')
    nextButton.click()
    time.sleep(2)

    
    


else:
     print('Le fichier ne sera pas envoyer')