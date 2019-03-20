# 1. Filters
names = ['zain', 'anthony', 'angel', 'billy']
names_start_a = list(filter(lambda n: n[0] == 'a', names))
print(names_start_a)

# 2. all
# prints true if everything in the genexp is
print(all(type(x) == str for x in ['Hello', 'Yello', 'Pillow']))
# True else prints false.

# 3. any
print(any(x % 2 == 0 for x in [1, 2, 3, 4]))

# 4. sorted
l = [1, 2, 3, 0]

print(sorted(l))
print(sorted(l, key=lambda x: x * x))
