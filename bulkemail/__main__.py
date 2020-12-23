from .bulk_email import BulkEmail
from .logger import Logger

# init logger
logger = Logger.getLogger()

# launch_code = BulkEmail.generate_launch_code(4)
# user_input = input(f"""You are about to email {BulkEmail.get_recipient_list()} people. Are you sure about this?
# Enter the following: {launch_code}
# -> """)
# if user_input != launch_code:  
#     print('Abort mission.')
#     exit()

BulkEmail.bulk_email()
logger.info(f'email sent to the following: {list(recipient for recipient in BulkEmail.get_recipient_list())}')
