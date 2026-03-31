import re
import string

d = [
    "12Race!car21",
    "!99An!na",
    "Banana",
    "!Rada!r!",
    "12345",
    "!De!eD!",
    "Python123",
    "!M!a!d!a!m!",
]

for key in d:
    d = [re.sub(r'[^\w\s]','',item) for item in d]

res= [re.sub(r'\d+', '', i) for i in d] 

def isPalindrome(s):
    return s == s[::-1]

print(isPalindrome("racedcar"))
