'''
Exercise 3.3.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of
values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a
space at the end, like this:
print('+', end=' ')
print('-')
The output of these statements is '+ -' on the same line. The output from the next print
statement would begin on the next line.
2. Write a function that draws a similar grid with four rows and four columns.
'''
#Answer 1

def row():
    print('+', '- ' * 4, end = '')
    print('+', '- ' * 4, end = '')

def post():
    print(('|' + ' ' * 9) * 2 + '|')

def do_four(f):
    f()
    f()
    f()
    f()
    
def column():
    do_four(post)

    
def grid():
    row()
    print('+')
    column()
    row()
    print('+')
    column()
    row()
    print('+')

grid()

