from selenium import webdriver
from getpass import getpass
import time
import xlsxwriter
#Connexion
username = 'Armanes'#input("Entrez le nom d'utilisateur :")
password = 'Shurke15'#getpass("Entrez le mot de passe :")

driver =  webdriver.Chrome(executable_path="C:\\Users\\Utilisateur\\Downloads\\chromedriver_win32\\chromedriver.exe") #Users\\ibay4\\Downloads\\chromedriver_win32\\chromedriver.exe"""
driver.get('https://www.ecoledirecte.com/Eleves/8136/Notes')

username_textbox = driver.find_element_by_id('username')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id('password')
password_textbox.send_keys(password)

login_button = driver.find_element_by_id('connexion')
login_button.click()
time.sleep(5)
##


#Récupération des thead
thead = driver.find_elements_by_css_selector('th')
tableHead = []
for i in range(len(thead)):
    tableHead.append(thead[i].text)
print(tableHead)
##
#Récupération de toutes les cellules (2ème semèstre)
table = driver.find_elements_by_css_selector('td')
table2=[]
for i in range(len(table)):
     table2.append(table[i].text)
print(table2)

##

#Récupération de toutes les cellules (1er semèstre)

semester1 = driver.find_element_by_css_selector("a[ng-click=\"setSelectedPeriode(\'#periode\'+$index, periode)\"")
semester1.click()
table = driver.find_elements_by_css_selector('td')
table1 = []
for i in range(len(table)):
     table1.append(table[i].text)
print(table1)
##

#Ecriture dans un fichier xlsx

workbook = xlsxwriter.Workbook("Test.xlsx")
bold = workbook.add_format({'bold': True})
worksheet = workbook.add_worksheet()


ligne = 0
col = 2

for element in (tableHead):
    worksheet.write(ligne, col, element, bold)
    col += 1

ligne = 1
col = 2

for element in (table1):
     if element=='':
          ligne += 1
          col=2
     elif element=='note(x)':
          break
     else:
          worksheet.write(ligne, col, element,)
          col += 1

worksheet2 = workbook.add_worksheet()


ligne = 0
col = 2

for element in (tableHead):
    worksheet2.write(ligne, col, element, bold)
    col += 1

ligne = 1
col = 2

for element in (table2):
     if element=='':
          ligne += 1
          col=2
     elif element=='note(x)':
          break
     else:
          worksheet2.write(ligne, col, element)
          col += 1



workbook.close()
driver.close()