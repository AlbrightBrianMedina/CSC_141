# Tough and difficult
class Resturaunt:
    """Model a resturaunt with OOP """
    def __init__(self, restaurant_name, cusuine_type, location, price_range, mascot):
        self.resturaunt_name = restaurant_name
        self.cusuine_type = cusuine_type
        self.location = location
        self.price_range = price_range
        self.mascot = mascot
        self.number_served = 78
        

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

    def resturaunt(self):
        print(f"We have served {self.number_served} customers today.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self):
        self.number_served += 60

cici_place = Resturaunt("Cici's Shack", "Soul Food", "Philadelphia", 20, "Cici",)
# cici_place.can_you_take_a_date() 
cici_place.set_number_served(98)
cici_place.increment_number_served()
cici_place.resturaunt() 