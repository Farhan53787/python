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
                contact.append(int(input("Enter date of birth: ")))
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