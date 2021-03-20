'''
    需要安装 pyEmail
'''

import smtplib
import email.mime.multipart
import email.mime.text
from setting import *


def sendEmail(reciever_email, title, content):
    try:
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = email_sender
        msg['to'] = reciever_email
        msg['subject'] = title

        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)

        smtp = smtplib.SMTP()
        smtp.connect(email_smtp_server)
        smtp.login(email_sender, email_sender_smtp_pass)
        smtp.sendmail(email_sender, reciever_email, str(msg))
        smtp.quit()
        print("Sending email success")
    except Exception as e:
        print(e)
        print("Sending email fail")
        return False




