# check if one string is substring of another

s = 'abcdefghijklmnop'
t= 'defno'

if t in s:
    print(t, 'found in string', s)
else:
    print(t, 'not found in string', s)


# remove spaces from left and right side of the string

name = "        abc             "
print(name.strip())

# remvoe from right side only 

print(name.rstrip())
print(name.lstrip())

