def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'red')
    if type(color) is not str:
        raise TypeError('color must be an instance of str')
    if type(text) is not str:
        raise TypeError('text must be an instance of str')
    if color not in colors:
        raise ValueError('color is invalid color')
    print(f'Printing {text} in {color}')


colorize('hello', 'red')
