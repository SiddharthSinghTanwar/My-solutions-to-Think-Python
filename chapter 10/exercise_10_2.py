"""Write a function called cumsum that takes a list of numbers and returns the cumulative sum; 
that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""
t = [1,2,3]
def cumsum(t):
    cum_sum = []
    element_sum = 0
    for item in t:
        element_sum += item
        cum_sum.append(element_sum)
    
    return print(cum_sum)
cumsum(t)




