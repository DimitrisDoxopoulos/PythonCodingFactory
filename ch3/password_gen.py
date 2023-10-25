# password generator
import string
import random

characters = list(string.ascii_letters + string.digits + ' !@#$%^&*()')

def generate_password():
    password_length = int(input('How long would you like yor password to be?'))
    random.shuffle(characters)
    password = []

    for i in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = ''.join(password)

    print(password)


def main():
    while True:
        option = input("Do you want to create a password? ('y' - 'Y' to generate or 'q' - 'Q' to quit\n")
        if option.lower() == 'y':
            generate_password()
        elif option.lower() == 'q':
            print('Good-Bye')
            break
        else:
            print('wrong Input')


if __name__ == '__main__':
    main()
