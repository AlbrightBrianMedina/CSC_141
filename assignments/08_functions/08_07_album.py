def make_album(musician, album_name, number_of_songs = None):
    if number_of_songs is None:
        return {musician : album_name}
    else:
        return {musician : (album_name, number_of_songs)}

print(make_album("Oscor", "Space Album"))
print(make_album("Panama", "Color Theory", 10))
print(make_album("Lil' Scooter", "Speed Demon", 11))