import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def send_mail_multiple(list_of_files,email,user_name):
    emailfrom = "ch.email.456@gmail.com"
    emailto = email

    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = user_name+" Your Files"
    msg.preamble = user_name+" Your Files"
    msg.attach(MIMEText("Your Files:- "))

    for fileToSend in list_of_files:
        ctype, encoding = mimetypes.guess_type(fileToSend)  # 1
        if ctype is None or encoding is not None:  # 1
            ctype = "application/octet-stream"  # 1

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":  # 1
            fp = open(fileToSend)  # 1
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)  # 1
            fp.close()  # 1
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)  # 1
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend.split("\\")[-1])  # 1
        msg.attach(attachment)  # 1

    server = smtplib.SMTP_SSL("smtp.gmail.com")
    # server.starttls()
    server.login("email", "password")
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()
