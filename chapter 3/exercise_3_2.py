'''
Exercise 3.2.
1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
function twice, passing the value as an argument.
3. Copy the definition of print_twice from earlier in this chapter to your script.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
argument.
5. Define a new function called do_four that takes a function object and a value and calls the
function four times, passing the value as a parameter. There should be only two statements in
the body of this function, not four.
'''
#Answer 1
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)
#Answer 2
def do_twice(f, val):
    f(val)
    f(val)
#Answer 3
def print_twice(bruce):
    print(bruce)
    print(bruce)
#Answer 4
do_twice(print_twice, 'spam')
#Answer 5
def print_once(colin):
    print(colin)

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)
do_four(print_once, 'spam')