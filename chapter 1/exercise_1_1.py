'''
Exercise 1.1. 
1. In a print statement, what happens if you leave out one of the parentheses, or both?
2. If you are trying to print a string, what happens if you leave out one of the quotation marks,
or both?
3. You can use a minus sign to make a negative number like -2. What happens if you put a plus
sign before a number? What about 2++2?
4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python?
What about 011?
5. What happens if you have two values with no operator between them?
'''
#Answer 1
print 'hello, world'
#Error: SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello, world')?
print('hello, world'
# The cursor keeps on going on the new line until the missing bracket is provided.

#Answer 2
print('this is me)
#SyntaxError: EOL while scanning string literal
print(hello world)
#SyntaxError: invalid syntax

#Answer 3
>>>2++2
4

#Answer 4
>>011
#SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

#Answer 5
>>>2 4
#SyntaxError: invalid syntax
