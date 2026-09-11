#This is what the program is doing. 
list_of_current_consoles = ["Nintendo Switch", "Xbox One", "Playstation 5", "PC"]

message = f"What I want for christmas is a {list_of_current_consoles[0].title()}"
print(message)
message = f"I prefer a {list_of_current_consoles[1].title()}"
print(message)
message = f"I usually use a {list_of_current_consoles[2].title()}"
print(message)
message = f"I like using a {list_of_current_consoles[3].title()}"
print(message)

print()
list_of_current_consoles[2] = "Steam Deck"
print(list_of_current_consoles)

print()
list_of_current_consoles.insert(0, "Mobile")
list_of_current_consoles.insert(3, "Linux")
list_of_current_consoles.append("Plug N' Play")

print()
removed_item = list_of_current_consoles.pop()
print (f"Sorry, but I don't really want a {removed_item}")

print()
print(sorted(list_of_current_consoles))
list_of_current_consoles.reverse()
list_of_current_consoles.sort()
list_of_current_consoles.sort(reverse=True)

print()
print(f"We have about {len(list_of_current_consoles)} items we want to get")

