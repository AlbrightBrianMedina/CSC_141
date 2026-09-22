"""
Brian Medina

Remaking a menu using a for loop after making a intentional error
"""

menu_order = ("Beef stew", "Grilled Cheese", "Rice", "Chicken", "Sandwhich")
print("Original Menu")
for food in menu_order:
    print(food)
#menu_order[0] = "something" 

print("\n")

menu_order = ("Beef stew", "Grilled Cheese", "Rice", "Pizza", "Steak")
print("New Menu")
for food in menu_order:
    print(food)