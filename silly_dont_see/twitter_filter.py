users = [
    {'username': 'samuel', 'tweets' : ['Hey', 'You']},
    {'username': 'katie', 'tweets' : []},
    {'username': 'jacob', 'tweets' : []},
    {'username': 'kiaran', 'tweets' : ['I\'m Kiaran you', 'What\'s your name?']},
]

inactive_users = list(u['username'] for u in filter(lambda u : not u['tweets'], users))
print(inactive_users)