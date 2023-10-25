# Regular exp module
import re

stack = []
num = 0

def push(list, item):
    list.append(item)

def pop(list):
    if list:
        return list.pop()
    else:
        print('Stack is empty')

def print_menu():
    print('1. Insert on top')
    print('2. Get from top')
    print('3. q/Q for Quit')

def get_choice():
    return input("Please provide a choice\n")

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:   
        print_menu()
        choice = get_choice()
        if not choice:
            continue
        
        # if choice in ['q', 'Q']:
        if choice == 'q' or choice == 'Q':
            break

        # r creates a regular expression
        pattern = r'^\d$'
        valid = re.match(pattern, choice)

        if not valid:
            print('Error in choice\n')
            continue

        num_choice = int(choice)

        match num_choice:
            case 1:
                num = input('Please insert a number\n')
                pattern_2 = '^\d+$'
                valid_2 = re.match(pattern_2, num)

                if not valid_2:
                    print('Please insert a number\n')
                    continue

                num = int(num)
                push(stack, num)
                print(f'{num} inserted\n')
                print()
            case 2:
                out_num = pop(stack)
                print(f'{out_num} is your lucky number\n')
                print()
            case _:
                print('Not a vlaid choice\n')

if __name__ == '__main__':
    main()