import re
import string

d = [
    "12Race!car21",
    "!99An!na",
    "Banana",
    "!Rada!r!",
    "12345",
    "!De!ed!",
    "Python123",
    "!M!a!d!a!m!",
]

for key in d:
    d = [re.sub(r'[^\w\s]','',item) for item in d]

res= [re.sub(r'\d+', '', i) for i in d] 

def isPalindrome(s):
    return s == s[::-1]

res2 = list(map(str.lower, res))

print(res2)

for i, j in zip(res, res2):
    if isPalindrome(j):
        print(i + " is a palindrome")
    else:
        print(i + " is no palindrome")