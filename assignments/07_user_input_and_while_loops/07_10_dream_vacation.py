# Brian Medina
#
# Where do you wanna go? 

responses = {}

while True:
    name = input("\nWhat is your name? ")
    response = input("Where is your dream vacation? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    while repeat != 'no' and repeat != 'yes':
        repeat = input() 
    if repeat == 'no':
        break       

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}. ") 