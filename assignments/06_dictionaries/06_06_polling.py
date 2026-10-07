"""
 Brian Medina

 Languages of Code
 Making a dictionary of people's favorite languages 
"""

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
lst_people = ['jen', 'sarah', 'bob', 'ken', 'pablo']

for i in lst_people:
    if i in favorite_languages:
        print (f'Thank you for your response, {i}.')
    else:
        print(f'We invite you to take a poll, {i}')