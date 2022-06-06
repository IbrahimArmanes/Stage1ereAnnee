import smtplib
from email.message import EmailMessage
from getpass import getpass


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
