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
    "!M!a!d!a!m!"
]

for key in d:
    if key != '!':
        d = [re.sub(r'[^\w\s]','',item) for item in d]

        

print(d)
