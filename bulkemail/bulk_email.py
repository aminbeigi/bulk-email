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

ATTACHMENTS_PATH = 'attachments/'

class BulkEmail:
    sender_email_address = ConfigParser.get('EMAIL', 'email_address')
    sender_email_password = ConfigParser.get('EMAIL', 'email_password')
    recipient_lst = json.loads(ConfigParser.get('EMAIL', 'recipient_list'))
    attachment_lst = json.loads(ConfigParser.get('EMAIL', 'attachments'))

    @classmethod
    def bulk_email(cls, subject, body):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(cls.sender_email_address, cls.sender_email_password)
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = cls.sender_email_address
            msg.set_content(body)

            for attachment in cls.attachment_lst:
                with open(ATTACHMENTS_PATH + attachment, 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name
                    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

            for recipient in cls.recipient_lst:
                smtp.send_message(msg=msg, to_addrs=recipient)
    
    @classmethod
    def get_recipient_list(cls):
        return cls.recipient_lst

    @staticmethod
    def generate_launch_code(length=4):
        alphabet = string.ascii_uppercase
        launch_code = ''
        for i in range(length):
            if i % 2 == 0 and i != 0: launch_code += ' '
            launch_code += random.choice(alphabet)
        return launch_code