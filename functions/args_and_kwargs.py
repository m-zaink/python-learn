def sum_of_all(*args):          # Tuple is passed into args
    return sum(args)


def fav_people(**kwargs):       # Dictionary is passed into kwargs
    for k, v in kwargs.items():
        print(f'{k}:{v}')


print(sum_of_all(1, 2, 3, 4, 5))    # any number of args
fav_people(colt='purple', zaink='black', ethel='teal')  # any number of args

print(sum_of_all)

