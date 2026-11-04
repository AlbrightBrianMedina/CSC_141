def make_album(musician, album_name, number_of_songs = None):
    if number_of_songs is None:
        return {musician : album_name}
    else:
        return {musician : (album_name, number_of_songs)}

responses = {}

while True:
    artist_name = input("What is the name of the artist?")
    reponse = input("What is the name of the album?")

    responses[artist_name] = reponse

    repeat = input("Have you finished entering your information? (yes/no)")
    while repeat != "no" and repeat != "yes":
        repeat = input()
    if repeat == "yes":
        break

print("The updated album list is now:")
for musician, album_name in responses.items():
    print(make_album(musician, album_name))