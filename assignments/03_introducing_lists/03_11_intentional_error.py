#This is what the program is doing. 
""" 
list_of_current_consoles = ["Nintendo Switch", "Xbox One", "Playstation 5", "PC"]

message = f"What I want for christmas is a {list_of_current_consoles[0].title()}"
print(message)
message = f"I prefer a {list_of_current_consoles[20].title()}"  <----
print(message)
message = f"I usually use a {list_of_current_consoles[7].title()}" <----
print(message)
message = f"I like using a {list_of_current_consoles[11].title()}" <----
print(message)

"""
"""
I have changed the index to numbers that does not exist in the list, so that is creating errors
"""
list_of_current_consoles = ["Nintendo Switch", "Xbox One", "Playstation 5", "PC"]



message = f"What I want for christmas is a {list_of_current_consoles[0].title()}"
print(message)
message = f"I prefer a {list_of_current_consoles[0].title()}"
print(message)
message = f"I usually use a {list_of_current_consoles[1].title()}"
print(message)
message = f"I like using a {list_of_current_consoles[3].title()}"
print(message)