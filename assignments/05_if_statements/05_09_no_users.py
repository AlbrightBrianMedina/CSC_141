"""


statements with usernames
"""

users = []

for user in users:
    if user.lower() == "admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print( "You're just some regular person") 
if len(users) == 0:
    print("We need more users!")