# Declare and initialize an array of names
names = ["John", "Jane", "Jack", "Jill"]

# Declare and initialize a two-dimensional array of numbers
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Traverse the names array using a for loop
for name in names:
    print(name)


# Traverse the numbers array using nested for loops
for row in numbers:
    for num in row:
        print(num)


# Concatenate the strings of the names array
concatenated_names = " ".join(names)
print(concatenated_names)



# Concatenate the numbers array
concatenated_numbers = " ".join(str(num) for row in numbers for num in row)
print(concatenated_numbers)
