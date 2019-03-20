# try:
#     foobar
# except:
#     print('Error')

# print('After error')


while True:
    try:
        num = int(input('Please enter a number : '))
    except ValueError as ve:
        print('That\'s not a number!')
    else:
        print('Good job. You entered a number!')
        break
    finally:
        print('Runs no matter what!!')

print('Rest of the game logic')