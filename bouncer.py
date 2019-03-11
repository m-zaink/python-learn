age = int(input('Enter your age : '))

if (age):
    if age >= 21:
        print('Hey man. Welcome!!')
    elif age >= 18:
        print('Go in little man but stay clear of the drinks.')
    else:
        print('Sorry kid. You can\'t get in!')
else:
    print('Enter a valid age.')
