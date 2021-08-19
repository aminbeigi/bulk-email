from .bulk_email import BulkEmail
from .logger import Logger
import sys

if len(sys.argv) != 4:
    print("Usage: python -m bulkemail bulkemail/recipients.txt bulkemail/subject bulkemail/body")
    exit(1)

if __name__ == '__main__':
    # init logger
    logger = Logger.getLogger()
    with open(sys.argv[1], 'r') as f:
        recipients = [i.strip() for i in f.readlines()] 
        print(recipients)
    with open(sys.argv[2], 'r') as f:
        subject = f.read()
    with open(sys.argv[3], 'r') as f:
        body = f.read()

    if len(recipients) == 0:
        logger.warning("Recipient list is empty. Can't send any emails.")
        exit(1)

    launch_code = BulkEmail.generate_launch_code(length=4)
    user_input = input(f"""You are about to email {len(recipients)} {"people" if len(recipients)!=1 else "person"}. Are you sure about this?
    Enter the following: {launch_code}
    -> """)
    if user_input != launch_code:  
        print("Abort.")
        exit(0)

    BulkEmail.bulk_email(recipients, subject, body)
    logger.info(f'{recipients}')
