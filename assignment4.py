# Write a program to print the amount to be paid based on distance traveled
# distance = int(input("Enter distance traveled : "))
# if distance >= 0 and distance <= 100:
#     print("The cost is Ksh. 5.00")
# elif distance > 100 and distance <= 500:
#     print("The cost is Ksh. 8.00")
# elif distance > 500 and distance <= 1000:
#     print("The cost is Ksh. 10.00")
# elif distance > 1000:
#     print("The cost is Ksh. 12. 00")
# else:
#     print("Invalid distance")

# Formatted prints or outputs

# Write a program to calculate total electricity bill to be paid based on units consumed

units = float(input("Enter units consumed : "))
if units > 0 and units <= 50:
    cost = 0.50 * units
    print("Your usage is Ksh. {}".format(cost))
elif units > 50 and units <= 150:
    cost = 1.00 * units
    print("Your usage is Ksh. {}".format(cost))
elif units > 150 and units <= 250:
    cost = 1.20 * units
    print("Your usage is Ksh. {}".format(cost))
elif units > 250:
    cost = 1.50 * units
    print("Your usage is Ksh. {}".format(cost))
else:
    print("Invalid unit value entered.")

