
'''
Exercise 1.2. Start the Python interpreter and use it as a calculator.
1. How many seconds are there in 42 minutes 42 seconds?
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
mile in minutes and seconds)? What is your average speed in miles per hour?
'''
#Answer 1
>>> seconds = 42 * 60 + 42
>>> seconds
2562

#Answer 2
>>> miles = 10 / 1.61
>>> miles
6.211180124223602

#Answer 3
>>> avg_pace = seconds / miles
>>> avg_pace
412.482
>>> avg_pace / 60
6.874700000000001
>>> avg_speed = miles / (seconds / 60 / 60)
>>> avg_speed
8.727653570337614
