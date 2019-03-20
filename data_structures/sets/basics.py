# Sets don't allow duplicates
# Sets don't have any order for their entries

s = {1, 2, 3}   # signified by the curly braces
# or
s = set(range(1, 4))    # parameter needs to be iterable

print(s)

# Looping over sets

for x in s:
    print(x)

# Methods in Sets:

# 1. add
print('# 1. add')

s.add(4)
print(f's.add(4) : {s}')

# 2. remove
print('# 2. remove')

s.remove(4)

print(f's.remove(4) : {s}')

# 3. discard
print('# 3. discard')

s.discard(4)    # if 4 not present, no error is returned

# 4. copy

s_copy = s.copy()

print(s_copy)


# 5. clear
# s.clear()

# element in set
print(f'4 in s {4 in s}')

# SET MATH OPERATIONS
s1 = set('abcdef')
s2 = set('aeiou')

# 1. Union
print('1. Union')
print(s1 | s2)

# 2. Intersection
print('# 2. Intersection')
print(s1 & s2)

# 3. Set Differnce
print('# 3. Set Differnce')
print(s1 - s2)