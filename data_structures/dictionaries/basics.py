# Declaring a dictionary
# Method #1
# Notice the curly braces!
user = {'name' : 'm-zaink', 'age' : 20, 14: 'fav-#'}
# Method #2
user_m2 = dict(name = 'm-zaink', age = 20)  # Bad Way!

print(user)
print(user_m2)

# ITERATING OVER DICTIONARIES
# 1. Iterating over keys : 
print('# 1. Iterating over keys : ')
for k in user.keys():
    print(k)

# 2. Iterating over values : 
print('# 2. Iterating over values : ')
for v in user.values():
    print(v)

# 3. Iterating over items : 
print('# 3. Iterating over items : ')
for k, v in user.items():
    print(f'{k} : {v}')

# METHODS IN DICTIONARIES
print('# METHODS IN DICTIONARIES')
# Validating if a key is present in the key-set
print('# Validating if a key is present in the key-set')
print(f'{"name" in user.keys()}')
# OR
print(f'{"name" in user}')

# Clear()
# user.clear()

# Copy()
user_copy = user.copy()

# Fromkeys() : used for defaulting a list of keys to a same default value
print('# Fromkeys() : used for defaulting a list of keys to a same default value')

default_dict = {}.fromkeys(['name', 'age', 'fun'], 'unknown')

print('# Fromkeys() : used for defaulting a list of keys to a same default value')
print(default_dict)

# Get():
print(f'{user.get("name")})')
print(f'{user.get("No-idea")}')
