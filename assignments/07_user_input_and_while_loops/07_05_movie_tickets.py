# Brian Medina
#
# What to say if someone is young enough for a free ticket

active = True
while active:
    age_of_person = input('How old are you?:')
    if age_of_person == 'quit':
        break
    elif int(age_of_person) < 3:
        print('You can watch the movie for free.')
    elif int(age_of_person) >= 3 and int(age_of_person) <=12:
        print('Your ticker price is $10.')
    else:
        print('Your ticket price is $15.')