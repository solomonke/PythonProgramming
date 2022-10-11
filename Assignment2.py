# Create a list of six students and do the following operations
# Add two new students to make 8
# Show the fourth to the seventh student in the list
# Replace the third student with
# Check if a student exists. If not, add the student.

students_list = ["John", "Abraham", "Rachel", "Mary", "Gabriel", "Ben"]
new_student_list = ["Elizabeth", "Mike"]
students_list.extend(new_student_list)
print(students_list[3:7])
students_list[2] = "Nancy"
print(students_list)
if "Brian" not in students_list:
    students_list.append("Brian")
    print(students_list)

if "Gabriel" not in students_list:
    students_list.append("Gabriel")
    print(students_list)



