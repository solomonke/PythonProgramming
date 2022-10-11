# Looping
# Check for a limit and terminates when limit is reached.
# Repetitions - a block (group) of code is repeated if some conditions are true.
# Two types of loops: 1. for loop 2. while loop
# for loop

# Loop through a string
# name = "ModCom"
# for check in name:
#     print(check)
#
# Range function has three components: 1. starting point 2. limit 3. increment/decrement
for count in range(3, 10, 2):
    print(count)

# Loop through a list

# Break statement terminates loop if condition is met.
# Continue statement skips the item

# countries = ["Kenya", "South Africa", "Uganda", "Tanzania", "Burundi"]
# for country in countries:
#     if country == "Uganda":
#         continue
#     print(country)

# Write a code that will loop through a list of 10 counties in Kenya
# Then add counties with two names inside a new list
# Print the new list

# counties = ["Mombasa", "Uasin Gishu", "Tana River", "Taita Taveta", "Wajir", "Nyandarua", "Homa Bay", "Kiambu", "Nakuru", "Tharaka Nithi"]
# newCountyList = []
# for county in counties:
#     if " " not in county:
#         newCountyList.append(county)
#         print(newCountyList)

