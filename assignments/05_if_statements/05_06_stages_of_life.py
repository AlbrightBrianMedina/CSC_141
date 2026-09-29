"""
 Brian Medina

 Program for the output to change depending on the age of a person
"""
age_number = [2, 4, 13, 20, 65]
for i in age_number:
    print(f"age: {i}")
    if i < 2:
        print("This person is a baby")
    elif i >= 2 and i < 4:
        print("This person is a toddler")
    elif i >= 4 and i < 13:
        print("This person is a kid")
    elif i >= 13 and i < 20:
        print("This person is a teenager")
    elif i >= 20 and i < 65:
        print("This person is an adult")
    elif i >= 65:
        print("This person is an elder")