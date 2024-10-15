phonebook = {
    "adnan shaikh":"8983245401",
    "maqbool shaikh":"9850281380",
    "taberz maniyar":"9049057373"
    }

def search_number():
    name = input("Enter name to search -")
    if phonebook[name]:
        print(f"Phone number - {phonebook[name]}")
    else:
        print("Name not found in phonebook.")

def add_number():
    name = input("Enter Name -")
    number = input("Enter phone number -")
    phonebook[name] = number
    print("Contact added successfully!")

def delete_number():
    name = input("Enter name to delete:")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully!")
    else:
        print("Name not found in phonebook.")

def display_phonebook():
    print("Phonebook:") 
    for name,number in phonebook.items():
        print(f"{name}:{number}")

while True:
    print("\nPhonebook Options:")
    print("1.Search phone number")
    print("2.Add phone number")
    print("3.Delete phone number")
    print("4.Display phonebook")
    print("5.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        search_number()
    elif choice == "2":
        add_number()
    elif choice == "3":
        delete_number()
    elif choice == "4":
        display_phonebook()
    elif choice =="5":
        break           
    else:
        print("Invalid choice. Please try again.")                          
