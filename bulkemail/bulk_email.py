import smtplib
from email.message import EmailMessage
from .config_parser import ConfigParser
import json
import string
import random
import imghdr

"""Bulk email many recipients

This class will send one email to a large group at once.
"""

class BulkEmail:
    sender_email_address = ConfigParser.get('EMAIL', 'sender_email_address')
    sender_email_password = ConfigParser.get('EMAIL', 'sender_email_password')
    attachments_path = ConfigParser.get('FILESYSTEM', 'attachments_path')
    attachments_lst = json.loads(ConfigParser.get('EMAIL', 'attachments'))

    @classmethod
    def bulk_email(cls, recipients, subject, body):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(cls.sender_email_address, cls.sender_email_password)
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = cls.sender_email_address
            msg.set_content(body)

            for attachment in cls.attachments_lst:
                with open(f"{cls.attachments_path}/{attachment}", 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name
                    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

            for recipient in recipients:
                smtp.send_message(msg=msg, to_addrs=recipient)
    
    @staticmethod
    def generate_launch_code(length=4):
        alphabet = string.ascii_uppercase
        launch_code = ''
        for i in range(length):
            if i % 2 == 0 and i != 0: launch_code += ' '
            launch_code += random.choice(alphabet)
        return launch_code
