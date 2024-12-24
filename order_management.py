# menu list of cafe
menu = {
    'Burger': 80,
    'Tea': 40,
    'Orange Juice': 120,
    'Pizza': 500,
    'Drinks':80
}
# Greet and showing menu
print("Welcome to my cafe right ")
print("Here is the menu of our cafe: ")
print("Burger: 80\nTea: 40\nOrange Juice: 120\nPizza: 500\nDrinks: 80\n")
order_total = 0
item_x = input("Enter The Order You Want to Place = ")
if item_x in menu:
    order_total += menu[item_x]
    print(order_total)
else:
    print (f"Item You Order {item_x} is not available ")
another_order = input("Do you want To Place Order Again? (yes/No) ")
item_y = input("Enter the name of item you want to add =")
if another_order == "yes":
    order_total += menu[item_y]
    print(f"Your Order {item_y} has been added")
elif another_order == "no":
    print(f"Item You Order {item_x} is not available")
else:
    print("Order Again Or Exit ")
print(f"The total amount of your item is {order_total}")