# Brian Medina
#
# Making a profile in a def function


def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('george', 'washington',
                                location='usa',
                                field='presidency')
print(user_profile)