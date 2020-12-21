from bulkemail.bulk_email import BulkEmail

launch_code = BulkEmail.generate_launch_code(4)
user_input = input(f"""You are about to email {BulkEmail.get_recipient_list_length()} people. Are you sure about this?
Enter the following: {launch_code}
-> """)
if user_input != launch_code:  
    print("Abort mission.")
    exit()

BulkEmail.bulk_email()