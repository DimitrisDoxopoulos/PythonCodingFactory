def main():
    facto = 1
    n = int(input('Pleas insert an int: '))

    for i in range(1, n + 1):
        facto *= i

    print(f'{n}! = {facto:,}')


if __name__ == '__main__':
    main()
