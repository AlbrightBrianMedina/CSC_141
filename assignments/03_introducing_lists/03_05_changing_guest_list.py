#This is what the program is doing. 

guest_list=["Lebron James", "Abraham Lincoln", "George Lucas", "Walt Disney"]

message = f"You have been invited to my dinner party, {guest_list[0].title()}."
print(message)
print()
message = f"Here is my invitation for you, {guest_list[1].title()}."
print(message)
print()
message = f"Here, have a dinner party invitation {guest_list[2].title()}."
print(message)
print()
message = f"Come to my dinner party, {guest_list[3].title()}."
print(message)
print()

guest_list[2]="Darth Vader"

print(guest_list)