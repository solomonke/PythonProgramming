# GUI Programming (Graphical User Interface
# Tkinter module. Still used by banks. Others no longer use it.
# It had been replaced by web applications, android applications, and IoT
# We will use control structures: for loops and if conditions

from hospitalfunctions import insert_patient as patient


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


# from hospitalfunctions import insert_patient as patient


def input_menu():
    while True:
        menu()
        str_choice = str(input("Enter your choice: "))
        if str_choice == "1":
            from hospitalfunctions import insert_patient as patient, send_sms
            patient()
        elif str_choice == "2":
            from hospitalfunctions import search_patient as search
            search()
        elif str_choice == "3":
            from hospitalfunctions import delete_patient as delete
            delete()
        elif str_choice == "4":
            from hospitalfunctions import update_patient as update
            update()
        elif str_choice == "5":
            from hospitalfunctions import donate
            donate()
        elif str_choice == "6":
            print("Exiting the hospital system.")
            break
        else:
            print("Invalid choice.")


input_menu()
