"""
 Brian Medina

 Program for what to say if a username is taken
"""
current_users = ["Mark", "John", "Smith", "Ashley", "Michal"]
new_users = ["Jordan", "Mark", "Trent", "Smith", "Bob"]

for user in new_users:
    if user in current_users:
        print(f"Username {user} is already in use")
    else:
        print("That username is available")