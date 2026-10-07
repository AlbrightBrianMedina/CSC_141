"""
 Brian Medina

 Numbers Upon Numbers
 Everyone has their favorite numbers
"""

favorite_numbers = {'George': ['56','92'],
                    "Micheal": ['12','85'],
                    "Bob": ['25','49'],
                    'Pedro': ['84','13'],
                    "Chris": ['42','50'],}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")