"""
. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""
t = [1,2,3]
def is_sorted(t):
    t2 = t[:]
    t.sort()
    if t2 == t:
        return True
    return False
print(is_sorted(t))