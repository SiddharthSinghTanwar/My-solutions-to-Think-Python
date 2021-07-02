'''
This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
If there are 23 students in your class, what are the chances that two of them have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.
'''
import random
t = []
for i in range(0, 23):
    t.append(random.randint(1,365))


def has_duplicates(t):
    count= 0
    occurence = 0
    for item in t:
        
        for i in range(len(t)):
            if item == t[i]:
                count += 1
        if count>1:
            occurence += 1
        count = 0
    if occurence > 1:
        return occurence
    else:
        return False

judgememt = has_duplicates(t)
if judgememt != False:
    print('the number of occurences of students having multiple birthdays are:\n', judgememt)
else:
    print('no such occurence')


