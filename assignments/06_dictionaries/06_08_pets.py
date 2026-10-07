"""
 Brian Medina

 Informations about Pets
 M
"""

pets = [ 
{'Pet Name': 'Snuggles',
'Owner Name': 'Dan',
'Species': 'Dog',}
,
{'Pet Name': 'Cleo',
'Owner Name': 'Patricia',
'Species': 'Cat',}
,
{'Pet Name': 'Nibbles',
'Owner Name': 'George',
'Species': 'Hamster',}
]

for i in pets:
    print(f'This pet is named {i["Pet Name"]}, their species is a {i["Species"]}, and their owner is {i["Owner Name"]}.')