# Create an array (list)
arr = [10, 20, 30, 40]

# Access element (O(1))
print('Second elements:', arr[1])

# Insert at end
arr.append(50)
print('After append:', arr)

# Insert in specific index
arr.insert(2, 25)
print('After insert:', arr)

# Delete element
arr.remove(40)
print('After delete:', arr)

# Search
if 30 in arr:
	print('Found!')