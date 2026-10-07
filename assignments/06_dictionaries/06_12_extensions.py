"""
Brian Medina

This assignment just wanted me to reuse a program from this chapter and experiment with it.
"""

favorite_numbers = {'george': 56,
                    "micheal": 12,
                    "bobby": 25,
                    'pedro': 84,
                    "chris": 42,
                    'todo': 17,
                    'noodle': 8,}

for name, favnumber in favorite_numbers.items():
    print (f'my name is {name.title()} and my favorite number is {favnumber}')

for name, favnumber in favorite_numbers.items():
    print (f'[{name.upper()}] [{favnumber}]') 