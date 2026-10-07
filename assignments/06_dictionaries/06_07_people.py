"""
 Brian Medina

 Making a list of people with their dictionary of information and using a for loop to print their info
"""

list_of_people = [ 
{'First Name': 'Blake',
'Last Name': 'Williams',
'age': '19',
'City': 'Ghane'}
,
{'First Name': 'Will',
'Last Name': 'Westen',
'age': '35',
'City': 'Mexico City'}
,
{'First Name': 'Paul',
'Last Name': 'Ricky',
'age': '52',
'City': "Hampton"}
]

for i in list_of_people:
    print(f'My first name is {i['First Name']} and my last name is {i['Last Name']}. I am {i["age"]} years old and live in {i["City"]} city')

# {i['First Name']} , i is a stand in for the dictionary and whatever is in the '' is what I'm calling.