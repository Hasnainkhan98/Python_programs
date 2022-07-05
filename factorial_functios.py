import math


#To compute the given input and find the factorial of a given number:
def factorial (n):
    return (math.factorial(n))

num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))

num=num1+num2

print('The number to find factorial is',num)

print (f"The Factorial of {num} is :",factorial(num))

#To get the factors of the number:
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

print_factors(num)