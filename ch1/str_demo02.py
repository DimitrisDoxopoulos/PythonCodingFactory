s = 'Coding Factory'

# Len is overloaded so it can return the length of whatever we want
print(len(s))

# Simple For
for i in range(len(s)):
    print(s[i], end=" ")
print()

# enchanced for
i = 1
for char in s:
    print(char, end=" " * i)
    i += 1