msg = 'unlucky'
for x in range(1, 21):
    if x == 4 or x == 13:
        msg = 'unlucky'
    elif x % 2 == 0:
        msg = 'even'
    else:
        msg = 'odd'
    
    print(f'{x} is {msg}')
    
