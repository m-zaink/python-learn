# A simple demo list
demo_list = ['a', 1, 45, True, 6.77]

# Printing the complete demo_list in one go
print(f'demo_list : {demo_list}')

# Printing the lenght of the list
print(f'len(demo_list) : {len(demo_list)}')

print('----------------------------------------')
# A simple range 1(inclusive) - 10(not inclusive)
r = range(1, 10)

# Casting the range into a list and printing it
print('Range -> List')
print(f'list(r) : {list(r)}')

print('----------------------------------------')
# Creating a colors-list
colors = ['teal', 'black', 'green']

# Printing each color in the colors-list
print('For Loop')
for color in colors:    # colors = iterable
    print(color)    # pring each item , color = iterator

print('----------------------------------------')
# A simple numbers list
print('For Loop : Square')
numbers = [4, 6, 2, 9, 7, 10]
# Print the square of each number in the list
for num in numbers:
    print(num * num)


print('----------------------------------------')
# Using a while loop to print the list
print('While Loop')
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1