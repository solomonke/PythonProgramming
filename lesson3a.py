# Data Types
# Arrays - A collection of items
# Four types of arrays: lists, tuples, dictionaries, sets

# List Data Types
# They contain lists of changeable, ordered. allow duplicate items
# List items are enclosed inside squared brackets []
# Would be inside a variable
countries = ["Kenya", "Somalia", "Uganda", "Tanzania"]
numbers = [10, 20, 30, 40, 50]
instances = [True, False, False, True]

Counties = ["Nairobi", 47, "Mombasa", 1, True, 20.45]

# List Operations

# Check length of a list - use the length function len()
# Check type type()
print(len(countries))
print(type(countries))

# Accessing Items on a list
# You can use indexes to access a list. Indexing starts from zero. Are enclosed inside square brackets
# Range function - The first item in the range is included but the last item is excluded.
print(numbers[0])
print(countries[2])
print(countries[1:3])

fruits = ["mangoes", "apples", "bananas", "pineapples", "strawberries", "oranges"]
print(fruits[2:4])
print(fruits[5])

# Checking the existence of an element - we use the (in) operator
if "bananas" in fruits:
    print("There are bananas in the basket.")

if "grapes" not in fruits:
    print("There are no grapes in the basket.")

# Adding an element to a list
# Replacing an element in a list
# Adding a list to another list
# Append is the most used function in lists. It adds an element at the end of a list.

fruits.append("grapes")
print(fruits)

# Replacing an element

fruits[1] = "avocados"
print(fruits)
fruits.insert(1, "oranges")
print(fruits)

# Extend function combines lists - extend()

fruits.extend(countries)
print(fruits)

# Removing items from a list
# If you know the index you use a function called pop()
fruits.pop(7)
print(fruits)

# If you know the element and not the index, you use the remove function
fruits.remove("strawberries")
print(fruits)

# To remove every element in the list, you use the clear function
fruits.clear()
print(fruits)








