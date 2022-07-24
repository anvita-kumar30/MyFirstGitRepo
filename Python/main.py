import math
print("Hello World!")
print(5+8)
print(5**2)
#This is a comment
'''
This is a multiline comment
'''
print(math.gcd(3,6))
e=31
e=float(e)
print(e)
e=str(445)
print(type(e))
name="    Tony    "
#strip() ignores the spaces
print(name.strip())
print("Length of string is " + str(len(name)))
#format() function
animal="dog"
action="bite"
temp="Does your {0} {1}?".format(animal,action)
print(temp)
temp=f"Does your {animal} {action}?"
print(temp)
