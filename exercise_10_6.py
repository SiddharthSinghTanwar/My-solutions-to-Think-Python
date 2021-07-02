'''
 Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams
'''
str1 = 'siddharth' 
str2 = 'hsrithdda'
def is_anagram(str1, str2):
    if len(str2) != len(str1):
        return False
    for item in list(str1):
        if item not in list(str2):
            return False
    return True

print(is_anagram(str1, str2))