import smtplib
import stdiomask
password1= stdiomask.getpass()
print(password1)
sender_email ="sender_email@gmail.com"
receiver_email="receiver_email@gmail.com"
# password1=input(str("please enter your password:"))
messeage="work is done"

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,password1)
print("login suceesfull")
server.sendmail(sender_email,receiver_email,"text msg")
print("email has been sent to",receiver_email)
