'''Exercise 2.1. Try out in interactive mode and make errors on purpose to see what goes wrong.
1. We’ve seen that n = 42 is legal. What about 42 = n?
2. How about x = y = 1?
3. In some languages every statement ends with a semi-colon, ;. What happens if you put a
semi-colon at the end of a Python statement?
4. What if you put a period at the end of a statement?
5. In math notation you can multiply x and y like this: xy. What happens if you try that in
Python?
'''
#Answer 1
>>> 42 = n
#SyntaxError: cannot assign to literal

#Answer 2
>>> x = y =1
>>> x
1
>>> y
1
#value gets assigned to both x and y

#Answer 3
>>> x = 2;
>>> x
2
>>> x = x +3;
>>> x
5
#No visible changes

#Answer 4
>>> x = 4.
>>> x
4.0
# It becomes a floating point value

#Answer 5
>>> x = 8
>>> y = 9
>>> xy
# Traceback (most recent call last):
#   File "<pyshell#63>", line 1, in <module>
#     xy
# NameError: name 'xy' is not defined
>>> xy = 90
>>> x
8
# xy becomes a new variable