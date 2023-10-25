# Meaning of else in for

# If we have eggs, we can invite people to eat
# If not, ask the guests to bring some

sales = ['apples', 'oranges', 'bananas']

for item in sales:
    if 'eggs' in sales:
        print(item)
    else:
        print('Buy some egs')
        break
else:
    print('Come to eat')