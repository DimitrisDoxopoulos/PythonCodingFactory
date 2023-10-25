# Print Cities

def print_cities(*cities):
    for city in cities:
        print(city, end=", ")
    print()

def main():
    print_cities('Athens', 'Paris', 'London')
    print('Athens', 'Paris', 'London')
    print_cities('Berlin')

if __name__ == '__main__':
    main()