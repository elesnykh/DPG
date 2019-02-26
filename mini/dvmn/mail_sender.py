import smtplib #библиотека почтового протокола
import os

mail = open('mail.txt') #шаблон письма
mail_text=mail.read()
mail.close()

from_mail='evglesnykh@yandex.ru' 
to_mail="civilpost@gmail.com"
subj='Приглашение на курс'

#редактируем шаблон в переменной
new_mail=mail_text.replace('%website%','dvmn.org') 
new_mail=new_mail.replace('%friend_name%','Евдот')
new_mail=new_mail.replace('%my_name%','Евгений')
msg = ("From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n".format(from_mail, "".join(to_mail), "".join(subj))) #добавляем от кого куда и тему

new_mail=msg + new_mail
new_mail=new_mail.encode("utf-8") #перекодируем для отправки

login=os.getenv("LOGIN") #подгружаем пароль и логин из .env
passw=os.getenv("PASSWORD")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, passw)
server.sendmail(from_mail, to_mail, new_mail)
server.quit()
