import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def file_type(fileToSend):
        ctype, encoding = mimetypes.guess_type(fileToSend)  # 1
        if ctype is None or encoding is not None:  # 1
            ctype = "application/octet-stream"  # 1

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":  # 1
            fp = open(fileToSend)  # 1
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)  # 1
            maintype = "text/plain"
            fp.close()  # 1
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            maintype = "image/jpeg"
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
        return attachment,maintype