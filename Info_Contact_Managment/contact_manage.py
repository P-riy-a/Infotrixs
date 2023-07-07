#modules:
import os
import csv
import datetime

# Creating Title
def title():
    title = "Contact Management System"
    dot = "________________________________"

    print(title)
    print(dot)
    print()

#class creation
class contact_fun:
    field_name = ["Name", "Mob_no"] #columns name
    db_name = "contacts.csv"
    contact_data = [] #list to store data

    #define the created functions
    def create(self):
        os.system('cls')
        title()
        print("Create Contact")
        print("\n")

        #iterate the field_name to get data
        for fields in self.field_name:
            if fields == "Mob_no":
                # validate Mob_no to ensure it is of 10 digits
                while True:
                    Mob_no = input("Enter " + fields + ": ")
                    if len(Mob_no) == 10:
                        self.contact_data.append(Mob_no)
                        break
                    else:
                        print("Mobile number should be 10 digits. Try again.\n")
            else:
                details = input("Enter"+ fields + ":")
                print("")
                self.contact_data.append(details)

        #get data from the system
        Date = datetime.datetime.today()
        d = Date.strftime("%B %d %Y") #strftime() func is used to give the format of date
        self.contact_data.append(d)

        # Check if the contact name already exists
        with open(self.db_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == self.contact_data[0]:
                    print("\nContact with the same name already exists. Please try again.\n")
                    self.contact_data = []  # Clear the contact_data list
                    return

        #here, using above statements we will get success to get input from user.
        #Insert data into csv file.
        with open(self.db_name, 'a') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])
        
        self.contact_data = [] #using this statement we will clear the contact_data list to get more inputs.
        print("")
        print("Contact is added successfully".center(125))
        print("\n")

#View contacts
    def view(self):
        os.system('cls')
        title()

        print("Contacts:")
        print("_______")
        print("")

        count = 0
        with open(self.db_name, 'r') as file:
            read = csv.reader(file)
            for data1 in read:
                if len(data1) > 0:
                    count += 1
            print("total contacts: ", count)
            print('_______________________')
            print('')
        #if no contacts are found
        with open(self.db_name, 'r') as file:
            read =csv.reader(file)
            if os.path.getsize(self.db_name) == 0:
                print("No contacts".center(125))
            else:
                for fields in self.field_name:
                    print('{0:<8}'.format(fields).center(5), end= "\t\t")
                print('{0:<15}'.format("Date"))
                print('')
                print("")

                for data in read:
                    for item in data:
                        print('{:<10}'.format(item).center(8),end='\t\t')
                    print("")
        print("\n")
        input("\t Press enter key to continue...".center(120))
        os.system('cls')

    #search
    def search(self):
        os.system('cls')
        title()

        print("Search Contacts")
        print("-------------------")
        print("")

        self.contact_match = 'false'
        search_value = input("Enter your name: ")
        print("")

        #display fields name
        for fields in self.field_name:
            print('{0:<10}'.format(fields).center(1), end= "\t\t")
        print('{0:<10}'.format("Date"))
        print("")
        print("")

        #read database for match
        with open(self.db_name, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0: #to check empty row
                    if search_value == data[0]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0],data[1],data[2]).center(10))

        if self.contact_match == 'false':
            print("")
            print("no contact found".center(125))
        
        print("")

#delete function
    def delete(self):
        os.system('cls')
        title()

        print("Delete Contacts")
        print("-------------------")
        print("")

        self.contact_match = 'false'
        delete_value = input("Enter contact name you want to delete: ")
        updated_list =[] #empty list help to update database

    #Read file to get match of the searched name
        with open(self.db_name, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data)> 0:
                    if delete_value != data[0]:
                        updated_list.append(data)
                    else:
                        self.contact_match ='true'

        #conditions to delete matched contacts
        if self.contact_match == 'true':
            with open(self.db_name, 'w') as file:
                write = csv.writer(file)
                write.writerows(updated_list)
                print("")
                print("Contacta deleted succesfully")
                print("")
        
        if self.contact_match == 'false':
            print("")
            print("Contact not found")
    #update
    def update(self):
        os.system('cls')
        title()

        print("Update Contacts")
        print("____________")
        print("")

        self.contact_match = 'false'
        update_value = input("Enter the name you want to update: ")
        updated_data = []  # list to store the updated data

        # Read file to get the match of the searched name
        with open(self.db_name, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if update_value != data[0]:
                        updated_data.append(data)
                    else:
                        self.contact_match = 'true'
                        # validate Mob_no to ensure it is of 10 digits
                        while True:
                            mob_no = input("Enter the updated Mob_no for {}: ".format(update_value))
                            if len(mob_no) == 10:
                                data[1] = mob_no
                                break
                            else:
                                print("Mobile number should be 10 digits. Try again.\n")
                        updated_data.append(data)

        # conditions to update matched contacts
        if self.contact_match == 'true':
            with open(self.db_name, 'w', newline='') as file:
                write = csv.writer(file)
                write.writerows(updated_data)
                print("")
                print("Contact updated successfully".center(125))
                print("")

        if self.contact_match == 'false':
            print("")
            print("Contact not found".center(125))

    

#object of class
contact_obj = contact_fun()

#clear the console
os.system('cls')    
title()

while True:
    #Creating menu.
    print("1. View Contacts")
    print("2. Create Contacts")
    print("3. Search Contacts")
    print("4. Delete Contacts")
    print("5: Update Contacts")
    print("6: Exit")
    print("\n")
    option = int(input("Choose your option:"))

#Choosing options
    if option == 1:
        contact_obj.view()
        title()
        

    if option == 2:
        while True:
            contact_obj.create()
            ans = input("Do you want to create another contact? [Y/N]: ".center(125))
            if ans == 'Y' or ans == 'y':
                continue
            else: 
                break

        os.system('cls')
        title()   
    

    if option == 3:
        while True:
            contact_obj.search()
            print("")
            ans = input("Do you want to search another contact? [Y/N]: ".center(125))
            if ans == 'Y' or ans == 'y':
                continue
            else: 
                break

        os.system('cls')
        title()   

         

    if option == 4:
        while True:
            contact_obj.delete()
            print("")
            ans = input("Do you want to delete another contact? [Y/N]: ".center(125))
            if ans == 'Y' or ans == 'y':
                continue
            else: 
                break

        os.system('cls')
        title()   
        
    if option == 5:
        while True:
            contact_obj.update()
            print("")
            ans = input("Do you want to update another contact? [Y/N]: ".center(125))
            if ans == 'Y' or ans == 'y':
                continue
            else: 
                break

        os.system('cls')
        title()   

    if option == 6:
        break