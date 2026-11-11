class User:
    def __init__(self, first_name, last_name, location, age, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.favorite_color = favorite_color
        self.login_attempts = 2

    def describe_user(self):
        print(f"\nHello my name is {self.first_name} {self.last_name}.")
        print(f"I am {self.age} years old. I live in {self.location} and my favorite color is {self.favorite_color}")

    def greet_user(self):
        print(f"\nHello there {self.first_name} {self.last_name}")
        print(f"I have updated your profile to involve your new infomation about {self.location}, {self.age}, and {self.favorite_color}")

    def incremental_login_attempts(self):
        self.login_attempts += 1
        

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("George", "Pollywag", "Europe", "23", "Orange")
#user_1.describe_user()
#user_1.greet_user()
user_1.incremental_login_attempts()
user_1.incremental_login_attempts()
user_1.incremental_login_attempts()
user_1.incremental_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)

#user_2 = User("Britney", "Brights", "America", "35", "Purple")
#user_2.describe_user()
#user_2.greet_user()

#user_3 = User("Bobby", "Walkins", "Mexico", "52", "Green")
#user_3.describe_user()
#user_3.greet_user()