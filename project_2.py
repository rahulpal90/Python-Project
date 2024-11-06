# Contact Management Book.
# In This Project Can Add , Delete , View , Search, Update , All Contact(Means You Can Count the Contact).

# Useing Dictionary ,Condition Statement ,Input Statement, Formatind String.

# Creating Empty Dictionary.
contacts = {}

while True:
    print('\n Contact book')
    print('1,Crate Contact')
    print('2,View Contact')
    print('3,Update Contact')
    print('4,Delete Contact')
    print('5,Search Contact')
    print('6,Count Contact')
    print('7,Exit')
    
    
    Choice = input("Enter Your Choice:- ")  
    
    if Choice == "1":
        name = input("Enter Name :- ")
        if name in contacts:
            print(f"Contact Name :- {name} Already Exist!")
        else:
            age = input('Enter Age :- ')
            mobile = input('Enter Mobile :- ')
            Email = input('Enter Email :- ')
            contacts[name] = {'age' : int(age) , 'email' : Email , 'mobile': mobile}    # User Say Data Lay Kar Dictionary May Save Kar raha hu.
            print(F"Contact Name {name} has been Created Sucessfully!")
            
    elif Choice == '2':      
        name = input("Enter Contact Name to view :- ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name} ,Age:{age} , Mobile Number:{mobile}")
        else:
            print("Contact Not Found")
            
    elif Choice == '3':
        name = input("Enter name to Upade:- ")
        if name in contacts:
            age = input('Enter Age :- ')
            mobile = input('Enter Mobile :- ')
            Email = input('Enter Email :- ')
            contacts[name] = {'age' : int(age) , 'email' : Email , 'mobile': mobile}
        else:
            print('contact Not Found!')
            
    elif Choice == "4":
        name = input("Enter name to Delete:- ")
        if name in contacts:
            del contacts[name]
            print(f"Contact Name {name} has been Deleted Sucessfully")
        else:
            print("Contact Not Found")
      
    elif Choice == "5":
        search_name = input("Enter name to Search:- ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"found-{name} ,Age:{age}, mobile Number :{mobile} EmailId: {Email} ")
                found = True
        if not found:
            print("No Contact Found with the Name")
    
    elif Choice == "6":
        print(f"Total Contacts In Your Book {len(contacts)}")
    
    elif Choice == "7":
        print('Closing Contact Book')
        break
    else:
        print("Invaild  input")                    
                
                
            
            
            
            
          

