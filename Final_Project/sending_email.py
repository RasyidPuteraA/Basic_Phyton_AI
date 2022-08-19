
from multiprocessing import context
import smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import username_email,pass_email
from smtplib import SMTPException

read_data = open('Final_Project/data_email.txt','r')
x = read_data.readlines()


for receiver in x:
    #Massage
    msg = MIMEMultipart('alternative')
    msg['Subject']='Test STMPT Basic Pyhton'
    msg['From']='Muhammad Rasyid Putera Agung'
    msg['To']= receiver

    #template
    html = open("Final_Project/template.html")
    template = MIMEText(html.read(),'html')
    msg.attach(template)
    
    #Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
        server.login(username_email,pass_email)
        server.sendmail(
            from_addr=username_email,to_addrs=receiver,msg=msg.as_string()
        )
        server.quit()
        
        print('Email Terkirim')
