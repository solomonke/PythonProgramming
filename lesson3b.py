# Tuples
# It is unchangeable, ordered, and allows duplicates.
# It uses the normal brackets

courses = ("Android", "Data Science", "Python")
language = ("Python",)
print(type(courses))
print(type(language))

# Elements in a tuple are ordered you can use indexing to access them.
# Indexing starts from zero and uses square brackets

print(courses[1])

# Create a tuple of five schools then add three more schools to the tuple

schools = ("Kenya High", "Ngandu Girls", "Mary Leakey", "St. John Boys", "Alliance Girls")
x = list(schools)
new_schools = "Starehe Boys", "Jamuhuri High", "Moringa School"
x.extend(new_schools)
print(x)
schools = tuple(x)
print(schools)



