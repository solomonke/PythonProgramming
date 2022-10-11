# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = odd_numbers + even_numbers
# print(all_numbers)

# print([1,2,3] * 3)

# lotsofhellos = "hello" * 10
# print(lotsofhellos)


# The target of this exercise is to create two lists called x_list and y_list,
# which contain 10 instances of the variables x and y, respectively.
# You are also required to create a list called big_list,
# which contains the variables x and y, 10 times each,
# by concatenating the two lists you have created.

x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]
x_list = [x] * 3
y_list = [y] * 3
big_list = (x_list + y_list)
print(big_list)
print(type(big_list))

