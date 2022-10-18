# Writing into files

# Write to an existing file or create a new file on which to write

try:
    file = open("document.txt", "a")

    file.write("\nI love \nprogramming.")
finally:
    file.close()