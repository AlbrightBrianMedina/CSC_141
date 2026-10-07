"""
 Brian Medina

 Ideal vactional spots
 Making a dictionary of people and the places they would like to go to 
"""

favorite_places = [{'friends name': "paul",
                    'location': 'japan'},
                    {'friends name': 'krissie',
                     'location': 'china'},
                     {'friends name': 'fred',
                      'location': 'russia'}
]
for i in favorite_places:
    print(f'My friend {i["friends name"]} would love to go to {i["location"]}.')