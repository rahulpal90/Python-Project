# In This Project i use Dictinory and Conditional Statement.

# Creating dictionary to store Menu and Price.

Menu = {
    'Pizza' : 40,
    "Pasta" :40,
    "Chinese" :40,
    "Vada Pav" :15,
    "Idli" : 25,
    "Tea":10,
    "Coffee":12
    
}

#Greet
print(f"Welcome Apna Restaurant")
print("Pizza:- Rs.40\nPasta:- Rs.40\nChinese:- Rs.40\nVadaPav:- Rs.15\nIdli:- Rs.25\nTea:- Rs.25\nCoffee:- Rs.12 ")

Order_Total = 0

item_1 = input("Enter Name of item You Want to Order:- ")

if item_1 in Menu:
    Order_Total+=Menu[item_1]
    print(f"{item_1} has been added to your order")
else:
    print(f"Order{item_1} Not Avialable Yet")
    
another_order = input("Do You Want to add Another item ? Yes / No ") 
if another_order == "Yes" :
    item2 = input("Enter the Secound item = ")    
    if item2 in Menu:
        Order_Total += Menu[item2]
        print(f"Item2 Has been Added to Order")
    else:
        print(f"order item {item2} is not Avialable!")
print(f"The Total amount of item to is {Order_Total}")        


