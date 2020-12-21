import smtplib
from email.message import EmailMessage
from .static_config_parser import StaticConfigParser
import json
import string
import random

"""Bulk email many recipients

This class will send one email to a large group at once.
"""

class BulkEmail:
    sender_email_address = StaticConfigParser.get('EMAIL', 'email_address')
    sender_email_password = StaticConfigParser.get('EMAIL', 'email_password')
    recipient_list = json.loads(StaticConfigParser.get('EMAIL', 'recipient_list'))

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
        for _ in range(n):
            launch_code += random.choice(alphabet)
        return launch_code