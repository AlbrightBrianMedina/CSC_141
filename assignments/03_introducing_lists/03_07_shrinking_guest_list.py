#Readjusting the list to be smaller

guest_list=["Lebron James", "Abraham Lincoln", "George Lucas", "Walt Disney"]
print()
guest_list[2]="Darth Vader"
guest_list.insert(0, "Ted")
guest_list.insert(3, "Jeremy")
guest_list.append("Paul")
print(guest_list)


guest = guest_list.pop()
print(f"Sorry, {guest}, but I only had enough chairs for two and I sadly have to uninvite you.")
guest = guest_list.pop()
print(f"Sorry, {guest}, but I only had enough chairs for two and I sadly have to uninvite you.")
guest = guest_list.pop()
print(f"Sorry, {guest}, but I only had enough chairs for two and I sadly have to uninvite you.")
guest = guest_list.pop()
print(f"Sorry, {guest}, but I only had enough chairs for two and I sadly have to uninvite you.")
guest = guest_list.pop()

print("\n\n")

message = f"You are still invited, {guest_list[0].title()}."
print(message)
message = f"You are still invited, {guest_list[1].title()}."
print(message)
print()

"""
To pop an item
make variable
removed_name = list_name.pop()
then 
print(message here, {removed_name})
do it for each removed item.
"""

del guest_list[0]
del guest_list[0]

print(guest_list)

"""
To delete
del (variable name)(put in zero 0)
then print the list
"""