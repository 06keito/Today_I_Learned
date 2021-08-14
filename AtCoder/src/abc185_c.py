from math import factorial
L = int(input())
print(factorial(L-1) // factorial(11) // factorial(L-12))