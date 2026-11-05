# Tough and difficult
class Resturaunt:
    """Model a resturaunt with OOP """
    def __init__(self, restaurant_name, cusuine_type, location, price_range):
        self.resturaunt_name = restaurant_name
        self.cusuine_type = cusuine_type
        self.location = location
        self.price_range = price_range

    def describe_resturuaunt(self):
        print(f"The resturuaunt name is {self.resturaunt_name}.")
        print(f"The price is {self.price_range}.")

    def can_you_take_a_date(self):
        if self.price_range > 50:
            print(f"Don't embaress yourself. It's too expensive.")
        else:
            print(f"You can afford {self.resturaunt_name}.")

    def prefered_food(self):
        if self.cusuine_type == "Pizza":
            print(f"Oh yeah, pizza!")
        else:
            print(f"No pizza, no buy")

parker_restaurant = Resturaunt("Papa Johns", "Pizza", "Reading", 20)
brendan_resturaunt = Resturaunt("Dreaded Diner", "Burger and fries", "Delaware", 25)
colt_restaurant = Resturaunt("The Plaza", "Mexican", "Maryland", 70)

colt_restaurant.can_you_take_a_date() 
brendan_resturaunt.can_you_take_a_date()
parker_restaurant.can_you_take_a_date()

colt_restaurant.prefered_food()
brendan_resturaunt.prefered_food()
parker_restaurant.prefered_food()