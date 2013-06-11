# -*- coding: utf-8 -*-
import os.path
import datetime
import smtplib

from email import Encoders, MIMEBase, MIMEMultipart, MIMEText
from email.Utils import formatdate

def create_message(from_addr, to_addr, subject, body, attach_file):
    msg = MIMEMultipart.MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate()

    body = MIMEText.MIMEText(body)
    msg.attach(body)

    attachment = MIMEBase.MIMEBase("image","png")
    # 添付ファイルのデータをセットする
    file = open(attach_file,"rb")
    attachment.set_payload(file.read())
    file.close()
    Encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header("Content-Disposition","attachment", filename=attach_file)

    return msg

def send(from_addr, to_addrs, msg):
    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    smtp.close()


#if __name__ == '__main__':
#    from_addr = "tukiyo3+test@gmail.com"
#    to_addr = from_addr
#    subject = "mail test."
#    body = "hello"
#    msg = create_message(from_addr, to_addr, subject, body, "screen16.png")
#    send(from_addr, [to_addr], msg)
