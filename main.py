from selenium import webdriver
from getpass import getpass
import smtplib
from email.message import EmailMessage
import time
import xlsxwriter


#Connexion
username = 'Armanes' #input("Entrez le nom d'utilisateur :")#'Armanes'#
password = 'Shurke15' #getpass("Entrez le mot de passe :")#'Shurke15'#

driver =  webdriver.Chrome(executable_path="C:\\Users\\ibay4\\Downloads\\chromedriver_win32\\chromedriver.exe") #Users\\ibay4\\Downloads\\chromedriver_win32\\chromedriver.exe
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

semester1 = driver.find_element_by_css_selector("a[ng-click=\"setSelectedPeriode('#periode'+$index, periode)\"")
semester1.click()
table = driver.find_elements_by_css_selector('td')
table1 = []
for i in range(len(table)):
     table1.append(table[i].text)
print(table1)
##





#Ecriture dans un fichier xlsx


outWorkbook = xlsxwriter.Workbook("Test.xlsx")
worksheet = outWorkbook.add_worksheet()

#format
bold = outWorkbook.add_format({'bold': True})
center_bold = outWorkbook.add_format({'bold': True, 'align': 'center'})
coef = outWorkbook.add_format()
coef.set_font_script(1)
noteSur = outWorkbook.add_format()
noteSur.set_font_script(2)
##

#Variables
cells='FGHIJKLMNOPQRST'
lastCell='F'
nombreNotes=0

##


ligne = 0
col = 2

for element in (tableHead):
    worksheet.write(ligne, col, element, bold)
    col += 1

ligne = 1
col = 2

for i in range(len(table1)):
     if table1[i]=='':
          ligne += 1
          col=2
     elif table1[i]=='note(x)':
          break
     else:
          worksheet.write(ligne, col, table1[i])
          col += 1

worksheet2 = outWorkbook.add_worksheet()

ligne = 0
col = 2

for element in (tableHead):
    worksheet2.write(ligne, col, element, bold)
    col += 1

ligne = 1
col = 2

for i in range(len(table2)):
     #### Belles notes
     if table2[i]=='':
          colMin = col
          
          notes=table2[i-1].split(' ')
          print(notes)
          for j in range(len(notes)):
               
               if notes[j].startswith('('):
                    if notes[j-1].startswith('/'):

                         worksheet2.write_rich_string(ligne, col-1,notes[j-2],noteSur,notes[j-1])
                         col += 1
                    else:
                         col -= 1
                         worksheet2.write_rich_string(ligne, col-1,notes[j-1],coef,notes[j])
                         col += 1
               elif notes[j].startswith('/'):
                    col -= 1
                    worksheet2.write_rich_string(ligne, col-1,notes[j-1],noteSur,notes[j])
                    col += 1
               elif notes[j]=='':
                    pass
               else:
                    worksheet2.write(ligne, col-1,notes[j])
                    col += 1
          nombreNotes = col - colMin

          
     ####
          ligne += 1
          col=2
     
     elif table2[i]=='note(x)':
          break
     else :
          worksheet2.write(ligne, col, table2[i])
          col += 1


lastCell= cells[nombreNotes]
rangeCell = 'F1:'+lastCell+'1'
worksheet2.merge_range(rangeCell, 'EVALUATIONS', center_bold)


outWorkbook.close()

## Fin Ecriture dans un fichier xlsx

#Envoi par mail

accept = input("Envoyer le fichier contenant les notes par mail ? (y/n)")
while accept != 'y' and accept != 'n':
     accept = input("Veuillez entrer \"y\" pour envoyer par mail ou bien \"n\" pour ne pas envoyer")

if accept == 'y':
     mail_adress = input("Votre mail : ")
     mail_pass= getpass("Votre mot de passe : ")

     msg = EmailMessage()
     msg["Subject"] = 'Votre relevé de note'
     msg["From"] = mail_adress
     msg["To"] = input("Envoyer à : ")
     msg.set_content('Relevé de note :')

     with open("Test.xlsx", "rb") as f:
          file_data = f.read()
          file_type = "xlsx"
          file_name = f.name
     
     msg.add_attachment(file_data, maintype='application', subtype=file_type, filename= file_name)  

     with smtplib.SMTP_SSL("smtp.gmail.com", 465 ) as smtp:
          smtp.login(mail_adress, mail_pass)
          smtp.send_message(msg)



     
else:
     print('Le fichier ne sera pas envoyer')


driver.close()