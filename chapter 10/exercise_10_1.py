'''
Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''
t = [[1,2],[3],[4,5,6]]

def nested_sum(t):
    nested_sum = 0
    for item in t:
        nested_sum += sum(item)
    return nested_sum

print(nested_sum(t))
