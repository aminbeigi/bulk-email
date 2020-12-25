import smtplib
from email.message import EmailMessage
from .config_parser import ConfigParser
import json
import string
import random

"""Bulk email many recipients

This class will send one email to a large group at once.
"""

class BulkEmail:
    sender_email_address = ConfigParser.get('EMAIL', 'email_address')
    sender_email_password = ConfigParser.get('EMAIL', 'email_password')
    recipient_lst = json.loads(ConfigParser.get('EMAIL', 'recipient_lst'))
    attachemnt_lst = ConfigParser.get('EMAIL', 'attachments')

    @classmethod
    def bulk_email(cls, subject, body):   
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(cls.sender_email_address, cls.sender_email_password)
            for recipient in cls.recipient_lst:
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = cls.sender_email_address
                msg['To'] = recipient
                msg.set_content(body)
                smtp.send_message(msg)
    
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