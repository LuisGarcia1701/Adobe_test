import re

def valid_email_format(email):
    # Regular expression pattern to match valid emails
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@codechallenge\.com$'

    # Check if email starts with a letter
    if email[0].isalpha():
        # Check if email matches the pattern
        if re.match(pattern, email):
            print("Valid email.")
            return True
        else:
            print("Invalid email.")
            return False
    else:
        print("Invalid format: Email must start with a letter.")
        return False


# Type an email to verify
#email = input("Please enter an email address: ")
#valid_email_format(email)

