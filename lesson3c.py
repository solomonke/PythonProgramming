# Python Dictionaries
# It is a data type that holds a collection of keys with their values
# Properties: It is changeable, ordered, but does not allow duplicates
# JavaScript Object Notation (JSON) file is a dictionary
# Majorly used in APIs
# Created using braces {}

student = {
    "name": "Brian",
    "age": 20,
    "course": "Software Development",
    "gender": "Male",
    "courses": ["Android", "Python", "Machine Learning"]
}
# Accessing elements from a dictionary

print(student["name"])

x = student.keys()
print(x)

y = student.values()
print(y)

z = student.items()
print(z)

# Adding items to a dictionary

student["height"] = 1.8
print(student)

# Replace an existing value
student["course"] = "Cyber Security"
print(student)

student.pop("gender")
print(student)







