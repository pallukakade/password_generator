'''
Description:
   Generate a random strong password that is a mix of uppercase & lowercase letters,
   as well as numbers and of length 8 characters. A strong password to provides great security.


@Since    :  March 2021.
@Author   :  Pallavi Ninad Kakade
@Summary  :  As a programmer, I want to write a python program that will Generate a strong password which
             includes numbers, upper case & lower case letters.
'''


from random import choice


def generate_password(length):
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    temp_pwd = lower_alpha + upper_alpha + numbers
    password = ''.join(map(lambda x: choice(temp_pwd), range(length)))
    return password


def password_check(passwd):
    val = True
    if len(passwd) == 8:
        print('Valid Password length :  Generated Password  is of 8 characters ')
        val = True

    if len(passwd) > 8:
        print('Invalid Password length :  Password length is greater than 8 characters')
        val = False

    if len(passwd) < 8:
        print('Invalid Password length :  Password length is less than 8 characters ')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Invalid Password  :  Generated Password should have at least one number / digit ')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Invalid Password  :  Generated Password should have at least one uppercase letter ')
        val = False

    if not any(char.islower() for char in passwd):
        print('Invalid Password  :  Generated Password should have at least one lower case letter ')
        val = False

    return val


# Main Method
def main():
    passwd_length = 8
    password = generate_password(passwd_length)
    print('The system generated password is : ', password)
    if (password_check(password)):
        print('Valid Password Generator')
    else:
        print('InValid Password Generator')


# Driver Code
if __name__ == '__main__':
    main()
