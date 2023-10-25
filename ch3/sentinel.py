def main():
    ch = input('Please insert a char')
    
    while ch != '#':
        print(ch, " : ", ord(ch))
        ch = input('Please insert a char')
    
    print('Good-bye...')

if __name__ == '__main__':
    main()