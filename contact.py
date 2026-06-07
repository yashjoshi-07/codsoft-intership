contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    elif choice == "2":
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print("Phone:", details["Phone"])
            print("Email:", details["Email"])
            print("Address:", details["Address"])

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name]["Phone"] = input("New Phone: ")
            contacts[name]["Email"] = input("New Email: ")
            contacts[name]["Address"] = input("New Address: ")
            print("Contact updated!")
        else:
            print("Contact not found!")

    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")