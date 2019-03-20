# Tuples are immutable
# Tuples are valid keys in a dicitonary

vowels = tuple('aeiou') # parameter should be a iterable

# OR

vowels = ('a', 'e', 'i', 'o', 'u')

print(vowels)

# Methods in tuples : 
# 1. count
print(vowels.count('a'))

# 2. index
print(vowels.index('e'))


# Looping over tuples

for v in vowels:
    print(v)