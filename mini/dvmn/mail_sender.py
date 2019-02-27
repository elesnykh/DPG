import smtplib
import os

with open('mail.txt') as mail:
    mail_text=mail.read()


from_mail='evglesnykh@yandex.ru'
to_mail="civilpost@gmail.com"
subj='Приглашение на курс'


new_mail=mail_text.replace('%website%','dvmn.org')
new_mail=new_mail.replace('%friend_name%','Евдот')
new_mail=new_mail.replace('%my_name%','Евгений')
msg = ("\
From: {}\r\n\
To: {}\r\n\
Subject: {}\r\n\r\n\
".format(from_mail, to_mail, subj))

new_mail=msg + new_mail
new_mail=new_mail.encode("utf-8")

login=os.getenv("LOGIN")
passw=os.getenv("PASSWORD")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, passw)
server.sendmail(from_mail, to_mail, new_mail)
server.quit()
