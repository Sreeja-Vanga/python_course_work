#calling a file with function in another file:
'''import logic
print(logic.add(5,6))
print(logic.sub(5,6))
print(logic.mul(5,6))
print(logic.div(5,6))
print(logic.rem(5,6))
print(logic.exp(5,6))'''

#using a var as alias to call the functions in the file:

'''import logic as lg
print(lg.add(5,6))
print(lg.sub(5,6))
print(lg.mul(5,6))
print(lg.div(5,6))
print(lg.rem(5,6))
print(lg.exp(5,6))'''

#to import specific functions:
'''
from logic import add,sub
print(add(5,6))
print(sub(5,6))'''

#to import all functions from another file:

from logic import *
print(add(5,6))
print(sub(5,6))
print(mul(5,6))
print(div(5,6))
print(rem(5,6))
print(exp(5,6))

