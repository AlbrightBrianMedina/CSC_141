# Brian Medina
#
# Just using 3 examples of organized code

"""I pretty much have been doing this automatically for a long time now. 
It just wants me to pretty much and organize my code"""

def display_message():
    message = "Hello there, new user!"
    print(message)
    print("Welcome to python!")

display_message()



def favorite_book(title):
    print(f"My favorite book is {title}!")

favorite_book("How To Do Origami")


def make_album(musician, album_name, number_of_songs = None):
    if number_of_songs is None:
        return {musician : album_name}
    else:
        return {musician : (album_name, number_of_songs)}

print(make_album("Oscor", "Space Album"))
print(make_album("Panama", "Color Theory", 10))
print(make_album("Lil' Scooter", "Speed Demon", 11))