# Optional Parameters

def get_formatted_date(day = 1, month = 1, year = 2000):
    print(f'{day:02d}/{month:02d}/{year:04d}')

def main():
    print(get_formatted_date())
    print(get_formatted_date(10))
    print(get_formatted_date(12, 4))
    print(get_formatted_date(20, 10, 2023))
    print(get_formatted_date(year = 2021))
    print(get_formatted_date(year = 2023, day = 13, month = 4))

if __name__ == '__main__':
    main()
