"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
#import regex as re

#def XO(txt):
#  count_o = len(re.findall("o", txt))
#  count_x = len(re.findall("x", txt))
#  if count_o ==count_x:
#    return True
#  elif count_o ==0 or count_x == 0:
#    return True
#  else:
#    return False

def XO(txt):
    x = txt.lower().count('x')
    o = txt.lower().count('o')
    return x == o

print(XO('we'))