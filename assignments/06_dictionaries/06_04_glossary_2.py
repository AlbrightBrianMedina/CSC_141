"""
 Brian Medina

 An extended list of glossary commands and using a loop to print it
"""

commands = {'print': 'This will print to screen.',
            'range': 'Output a range of numbers.',
            'if': 'Is something true of false',
            'variable': 'something that holds data',
            'string': 'In array of characters',
            'syntax': 'Set of rules of how codes should be structured and written.',
            'for loop': 'It cycles through a list/dictionary/values/data/etc',
            'len': "Returns of the length of a string"}
for i in commands:
    print(f'The command is {i}: \n and the defininition is {commands[i]}\n')

"""
For loop goes through each key and prints it's value. 
"""