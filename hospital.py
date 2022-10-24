# GUI Programming (Graphical User Interface
# Tkinter module. Still used by banks. Others no longer use it.
# It had been replaced by web applications, android applications, and IoT
# We will use control structures: for loops and if conditions

# from hospitalfunctions import insert_patient as patient


def menu():
    text = "Welcome to Modcom Hospital\n " \
           "Please select a choice \n " \
           "1. Add Patient \n" \
           "2. Search a patient \n" \
           "3. Delete Patient \n" \
           "4. Update patient information \n" \
           "5. Donate \n" \
           "6. Exit"
    print(text)


def input_menu():
    menu()
    str_choice = str(input("Enter your choice: "))
    if str_choice == "1":
        from hospitalfunctions import insert_patient as patient
        patient()


input_menu()
