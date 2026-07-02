import sys

def phonebook(contact):
    row, col = int(input("Enter some contact numbers:")), 5

    phone_book = []
    print(phone_book)
    for i in range(row):
        print("Enter %d contact details" % (i + 1))
        contact = []
        for j in range(col):
            if j == 0:
                contact.append(str(input("Enter name: ")))
                if contact[j] == "" or contact[j] == " ":
                    sys.exit("Error: Name is mandatory.")
            elif j == 1:
                contact.append(int(input("Enter phone number: ")))
                if contact[j] == "" or contact[j] == " ":
                    sys.exit("Error: Phone number is mandatory.")

            elif j == 2:
                contact.append(str(input("Enter date of birth: ")))
                if contact[j] == "" or contact[j] == " ":
                    contact[j] = None
            elif j == 3:
                contact.append(str(input("Enter email address: ")))
                if contact[j] == "" or contact[j] == " ":
                    contact[j] = None

            elif j == 4:
                contact.append(str(input("Enter category of the owner of this number: ")))
                if contact[j] == "" or contact[j] == " ":
                    contact[j] = None

            phone_book.append(contact)

            print(phone_book)
            return phone_book

def menu():
    print("1. Add contact")
    print("2. View contacts")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    return choice

def add_contact(pb):
    dip=[]
    for i in range(len(pb)):
        if i == 0:
            dip.append(str(input("Enter name: ")))

        if i == 1:
            dip.append(int(input("Enter phone number: ")))

        if i == 2:
            dip.append(str(input("Enter date of birth: ")))

        if i == 3:
            dip.append(str(input("Enter email address: ")))

        if i == 4:
            dip.append(str(input("Enter category of the owner of this number: ")))

    pb.append(dip)

    return pb

def remove_contact(pb):
    query = str(input("Enter the name of the contact you want to delete: "))

    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("Contact deleted successfully.")
            return pb

    if temp == 0:
        print("Contact not found.")

    return pb

def search_contact(pb):
    choice = int(input("Enter ,1.Name, 2.Phone number, 3.Date of birth, 4.Email address, 5.Category, to search contact: "))
    temp = []
    check=-1
    if choice == 1:
        query = str(input("Enter the name of the contact you want to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
        if check == -1:
            print("Contact not found.")

    elif choice == 2:
        query = int(input("Enter the phone number of the contact you want to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
        if check == -1:
            print("Contact not found.")
    
    elif choice == 3:
        query = str(input("Enter the date of birth of the contact you want to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
        if check == -1:
            print("Contact not found.")
    
    elif choice == 4:
        query = str(input("Enter the email address of the contact you want to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
        if check == -1:
            print("Contact not found.")

    elif choice == 5:
        query = str(input("Enter the category of the contact you want to search: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])
        if check == -1:
            print("Contact not found.")
    
    else:
        print("Invalid choice.")
    return pb

def view_contacts(pb):
    if not pb:
        print("No contacts found.")
    else:
    for i in range(len(pb)):
        print(pb[i])

def exit():
    print("Exiting the program.")
    sys.exit()