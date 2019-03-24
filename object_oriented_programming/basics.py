class User:
    active_users = 0    # class attribute

    @classmethod
    def display_active_users(cls):
        return f'There are {clss.active_users} active users currently'

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(', ')
        return cls(first, last, age) 

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f'{self.full_name()} logged out'

    def full_name(self):
        return self.first + ' ' + self.last

    def initials(self):
        return self.first[0] + '.' + self.last[0]

    def likes(self, thing):
        return f'{self.first} likes {thing}'

user = User('Joi', 'Dawn', 25)

print(user.full_name())
print(user.initials())
print(user.likes('Croatia'))

new_user = User.from_string('Tom, Billow, 89')

print(new_user.full_name())