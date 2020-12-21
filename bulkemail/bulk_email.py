import smtplib
from email.message import EmailMessage
from .static_config_parser import StaticConfigParser

"""Bulk email many recipients

This class will send one email to a large group at once.
"""

class BulkEmail:
    sender_email_address = StaticConfigParser.get('EMAIL', 'email_address')
    sender_email_password = StaticConfigParser.get('EMAIL', 'email_password')

    @classmethod
    def bulk_email(cls):
        msg = EmailMessage()
        msg['Subject'] = 'Hello there'
        msg['From'] = cls.sender_email_address
        msg['To'] = cls.sender_email_address
        msg.set_content('an epic body for an epic email')
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(cls.sender_email_address, cls.sender_email_password)
            smtp.send_message(msg)
    