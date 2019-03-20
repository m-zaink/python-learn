# if - else for values
numbers = {x : ('even' if x % 2 == 0 else 'odd' ) for x in range(10)}
print(numbers)

# if - else for keys
numbers = {('even' if x % 2 == 0 else 'odd') : x for x in range(10)}
print(numbers)

ascii_pair = {x : chr(x) for x in range(65, 65 + 26)}

print(ascii_pair)