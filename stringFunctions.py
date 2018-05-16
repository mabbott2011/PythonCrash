# String Functions
myStr='Hello World'

print(myStr.capitalize())

#Swap case
print(myStr.swapcase())

# Length
print(len(myStr))

# Replace
print(myStr.replace('World', 'Everyone'))

# Number of occurances within String, case sensative
sub = 'H'
print(myStr.count(sub))
# l -> 3
# h -> 0
# H -> 1


# Starts with or ends with
print(myStr.startswith('Hello'))  # True
print(myStr.endswith('!')) # True
print(myStr.startswith('ello')) # False

# Split string into Lists
print(myStr.split())  # ['Hello', 'World!']

# FIND
print(myStr.find('World')) # 6  # found by 6th character
# INDEX  -  Similar to FIND but throws error if item isn't found
print(myStr.index('W')) # 6
#print(myStr.index('9')) # ValueError: substring not found

# Is all aphanumeric?
print(myStr.isalnum()) # False

# Is all alphabetic
print(myStr, 'is alphabetric?', myStr.isalpha()) # False, has a space
