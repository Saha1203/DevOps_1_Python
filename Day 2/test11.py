import re

text = "The quick brown fox"
pattern = r"qucik"

match  = re.match(pattern, text)
if match:
    print("Match found: ",match.group())
else:
    print("No match")