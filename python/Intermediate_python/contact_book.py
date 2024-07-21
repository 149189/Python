def add_contact(contacts):
    contact_id = max(contacts.keys(), default=0) + 1
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    contacts[contact_id] = {'name': name, 'phone': phone}
    print("Contact added successfully!")

def delete_contact(contacts):
    contact_id = int(input("Enter contact ID to delete: "))
    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact(contacts):
    search_name = input("Enter name to search: ")
    found_contacts = {cid: info for cid, info in contacts.items() if search_name.lower() in info['name'].lower()}
    if found_contacts:
        for cid, info in found_contacts.items():
            print(f"ID: {cid}, Name: {info['name']}, Phone: {info['phone']}")
    else:
        print("No contacts found!")

def view_contacts(contacts):
    if contacts:
        for cid, info in contacts.items():
            print(f"ID: {cid}, Name: {info['name']}, Phone: {info['phone']}")
    else:
        print("No contacts available.")

def main():
    contacts = {1: {'name': 'Kaustubh', 'phone': '8657092872'},
                2: {'name': 'Hemant', 'phone': '668687687'}}
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            delete_contact(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            view_contacts(contacts)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
