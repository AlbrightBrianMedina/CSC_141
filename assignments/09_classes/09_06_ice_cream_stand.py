# Tough and difficult
class Resturaunt:
    """Model a resturaunt with OOP """
    def __init__(self, restaurant_name, cusuine_type, location, price_range, mascot):
        self.resturaunt_name = restaurant_name
        self.cusuine_type = cusuine_type
        self.location = location
        self.price_range = price_range
        self.mascot = mascot

    def describe_resturuaunt(self):
        print(f"The resturuaunt name is {self.resturaunt_name}.")
        print(f"The price is {self.price_range}.")
        print(f"It's located by{self.location}")
        print(f"It normally serves {self.cusuine_type}")
        print(f"It's mascot is {self.mascot}")

    def can_you_take_a_date(self):
        if self.price_range <= 50:
            print(f"Don't embaress yourself. It's too expensive.")
        else:
            print(f"You can afford {self.Resturaunt}.")


class ice_cream_stand:
    def __init__(self, ice_cream_flavors):
        self.ice_cream_flavors = ice_cream_flavors


#cici_place = Resturaunt("Cici's Shack", "Soul Food", "Philadelphia", 20, "Cici")
cici_place = ice_cream_stand(["vanilla", "chocolate", "mint", "strawberry"])
print (cici_place.ice_cream_flavors)
#cici_place.can_you_take_a_date() 