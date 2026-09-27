"""


statements with usernames
"""

users = [ "Admin", "John", 'Alice', "Bob", 'Charlie']

for user in users:
    if user.lower() == "admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print( "You're just some regular person") 