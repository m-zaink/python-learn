numbers = {x for x in range(10)}
print('Numbers : ')
print(numbers)

even = {x for x in range(10) if x % 2 == 0}
print('Even Numbers : ')
print(even)

odd = {x for x in range(10) if x % 2 != 0}
print('Odd Numbers : ')
print(odd)


alter_odd_even = {'even' if x % 2 == 0 else 'odd' for x in range(10)}

print('alter_odd_even')
print(alter_odd_even)