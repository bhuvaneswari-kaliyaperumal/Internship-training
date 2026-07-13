contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print(f"{name} added successfully.\n")

def find_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        print(f"Phone Number: {contacts[name]}\n")
    else:
        print("Contact not found.\n")

def list_contacts():
    if not contacts:
        print("No contacts available.\n")
    else:
        print("\nContact List")
        print("-" * 25)
        for name, phone in contacts.items():
            print(f"Name : {name}")
            print(f"Phone: {phone}")
            print("-" * 25)

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Find Contact")
    print("3. List Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        list_contacts()
    elif choice == "4":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")