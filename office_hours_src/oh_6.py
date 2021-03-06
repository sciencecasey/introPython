'''
Created on Mar 2, 2021

@author: CaseyJayne
1. Write and call a function named "hello" that accepts no parameters and prints "Hello, world!" to the console.
2. Add and call a function named "add" that accepts two parameters "x" and "y", adds them, and prints "Result: X" to the console (where X is the result of adding the two parameters x and y).
3. Add and call a recursive function named "sum_of_squares" that accepts a single integer parameter N and recursively computes the sum of squares from 1 to N.  Print the single, resulting value to the console.  Ex: If N = 5, your function should return 55 because 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55.
'''

def hello():
    print("Hello world!")
    

def add(x, y):
    print("Result: " + str(x+y))


def sum_of_squares(n):    
    if n == 1:
        return 1**2
    else:
        return n**2 + sum_of_squares(n-1)

if __name__ == '__main__':
    hello()
    y = sum_of_squares(5)
    print(str(y))
    print("Adding")
    add(-1,6)
    