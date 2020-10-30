"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    
    return int(float(txt))

print(string_int("2"))
print(type(string_int("2")))


print(string_int("3.2"))
print(type(string_int("3.2")))


