# A simple program to print a triangle of smileys
# :D
for i in range(10):
    for j in range(i + 1):
        print('\U0001f600', end='')
    print()

# OR

for i in range(1, 11):
    print('\U0001f600' * i)
