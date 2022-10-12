contact = {}

def  display_contact(): #contact display function
    print("{Name\t\tcontact number")
    for key in contact:

        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice = int(input("1. Add new contact \n 2. search contact \n 3.Display contacts \n 4.edit contact \n 5.delete contact \n 6.Exit \n Enter your choice"))
    #gives choices for use experience
    if choice == 1:
        name = input("enter the contact name ")
        phone = input("enter the mobile number")
        contact[name]= phone
    elif choice == 2:
        search_name = input(" enter the contact name")
        if search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("enter the contact you want to edit")
        if edit_contact in contact:
            phone = input("enter mobile number")
            contact[edit_contact]= phone
            print("contact updated!")
            display_contact()
        else:
            print("name is not found")
    elif choice == 5:
        del_contact = input("enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact yes/no?")
            if confirm == "yes" or confirm == "no":
                contact.pop(del_contact)
                display_contact()
            else:
                print("name is not found in contact book")
        else:
            break


