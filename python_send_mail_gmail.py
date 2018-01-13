import smtplib as se
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


s = se.SMTP_SSL('smtp.gmail.com')
#s.starttls()

print ("success")
msg = MIMEMultipart('alternative')
msg['Form'] = "email@gmail.com"
msg['To'] = "email@gmail.com"
msg['Subject'] = "Done"
msg_part = MIMEText("hello world")
msg.attach(msg_part)
s.login("email@gmail.com","email1234567890")
s.sendmail("emai@gmail.com","email@gmail.com",msg.as_string())
print ("success 1")
s.quit()
