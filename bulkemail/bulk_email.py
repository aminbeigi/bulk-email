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
    recipient_list = json.loads(ConfigParser.get('EMAIL', 'recipient_list'))

    @classmethod
    def bulk_email(cls):   
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(cls.sender_email_address, cls.sender_email_password)
            for recipient in cls.recipient_list:
                msg = EmailMessage()
                msg['Subject'] = 'Hello there'
                msg['From'] = cls.sender_email_address
                msg['To'] = recipient
                msg.set_content('an epic body for an epic email')
                smtp.send_message(msg)
    
    @classmethod
    def get_recipient_list_length(cls):
        return len(cls.recipient_list)


    @staticmethod
    def generate_launch_code(n):
        alphabet = string.ascii_uppercase
        launch_code = ''
        for i in range(n):
            if i % 2 == 0 and i != 0: launch_code += ' '
            launch_code += random.choice(alphabet)
        return launch_code