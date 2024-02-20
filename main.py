# Imagine that you're writing application that requires user input and your responsibility is a functionality that will accept and validate user name and email.' \
# Please write a code that will prompt user for both name and email and verify is these fields meet following expectations:

# 1.User name can’t include any numeric characters (digits)
# 2.User name can’t exceed 15 characters
# 3.Email address must start with user name
# 4.All email letters must be in lower case (here I’d provide hint that, please note that username and email address case might be different)
# 5.Email address must end with `@ubs.com`
# 6.Email address must include underscore (`_`) character
# 7.Please validate that there are no whitespaces in email address


# # 1.User name can’t include any numeric characters (digits)

def contain_only_letters(s):
    return s.isalpha()
user_name = input('Please provide your user name:')
if contain_only_letters(user_name):
    print('User name contains only letters, good to go!')
else:
    print('User name must contain only letters, please provide correct user name!')

# 2.User name can’t exceed 15 characters

user_name = input("Please provide your user name:")
if len(user_name) > 15:
    print("Error! Only 15 characters are allowed for the user name")
else:
    print('User name has allowed length')

# 3.Email address must start with user name
def check_email_address(new_user_address: str):
    print(new_user_address)
    result = new_user_address.startswith(user_name)
    print(f'My current result: {result}')
    return result #True
user_email = input('Please provide your emial address')
if check_email_address(new_user_address=user_name):
    print("Address is correct")
else:
    print("Address is incorrect")

# 4.All email letters must be in lower case

def contain_only_lower_case(m):
    return m.islower()
user_email = input('Please provide your emial address')
if contain_only_lower_case(user_email):
    print("User address is correct!")
else:
    print("Error!User addres must contain only lower case!")

# 5.Email address must end with `@ubs.com`

def check_email_address(new_user_address: str):
    print(new_user_address)
    result = new_user_address.endswith('@ubs.com')
    print(f'My current result: {result}')
    return result #True
user_email = input('Please provide your emial address')
if check_email_address(user_email):
    print("Address is correct")
else:
    print("Address is incorrect")

# 6.Email address must include underscore (`_`) character
# 7.Please validate that there are no whitespaces in email address

def there_are_no_whitespaces(n):
    return n.isspace()
user_email = input('Please provide your email address')
if there_are_no_whitespaces(user_email):
    print("Address is correct!")
else:
    print("Error! Whitespaces are not allowed!")