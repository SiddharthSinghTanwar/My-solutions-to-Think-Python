'''
Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
'''
t = [1,2,3,3]
def has_duplicates(t):
    count= 0
    for item in t:
        if count>1:
            return True
        count = 0
        for i in range(len(t)):
            if item == t[i]:
                count += 1
        
    return False

print(has_duplicates(t))