data = [1, 2, 3]
print(f'Data (Original) : {data}')
# 1. Append
data.append(5)
print(f'Data (.append(5)) : {data}')

# 2. Extend
data.extend([10, 20, 50])
print(f'Data (.extend([10, 20, 50])) : {data}')

# 3. Insert
index = 2
data.insert(index, 'At Index 2')
print(f'Data (.insert(index, \'At Index 2\')) : {data}')

index = -1
data.insert(index, 'At Index -1')
print(f'Data (.insert(index, \'At Index -1\')) : {data}')

# ADVANCED LIST METHODS

# 4. Clear
# data.clear()
# print(f'Data (.clear()) : {data}')


# 5. Pop
print(f'data (.pop()) : {data.pop()}')
print(f'data (.pop(1)) : {data.pop(1)}')

# 6. Remove
data.remove(10)
print(f'data (.remove(10)) : {data}')

# 7. Index