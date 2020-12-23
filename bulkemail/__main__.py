from .bulk_email import BulkEmail
from .logger import Logger
from .config_parser import ConfigParser

# init logger
logger = Logger.getLogger()

if len(BulkEmail.get_recipient_list()) == 0:
    logger.warning('Recipient list is empty. Can\'t send any emails.')
    exit()

launch_code = BulkEmail.generate_launch_code(length=4)
user_input = input(f"""You are about to email {len(BulkEmail.get_recipient_list())} {'people' if len(BulkEmail.get_recipient_list())!=1 else 'persen'}. Are you sure about this?
Enter the following: {launch_code}
-> """)
if user_input != launch_code:  
    print('Abort mission.')
    exit()

subject = ConfigParser.config.get('EMAIL', 'Subject')
body = ConfigParser.config.get('EMAIL', 'body')

BulkEmail.bulk_email(subject, body)
logger.debug(f'{BulkEmail.get_recipient_list()}')