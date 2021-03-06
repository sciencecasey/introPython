'''
Created on Mar 3, 2021
Practicing nested functions, closures, and decorators
@author: CaseyJayne
https://www.programiz.com/python-programming/decorator

Note - go back to the last 1/3 of this article to review a bit more complex later
'''

def smart_divide(func): # this is a decorator function
    print("in smart divide")
    def inner(a, b):  # this is a nested function
        print("in nested check")
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return  # early out

        return func(a, b)
    return inner


@smart_divide # now this function is decorated
def divide(a, b):
    print("in divide")
    print(a/b)
    

def main():
    print("In decorate_funs main")
    print("Calling smart division, 4/2")
    smart_divide(divide(4, 2))
    print("Calling division, 4/2")
    divide(4, 2)
    print("Calling smart division, 4/0")
    smart_divide(divide(4, 0))
    print("Calling division, 4/0")
    divide(4, 0)
    
if __name__=="__main__":
    main()
else: 
    print(__name__)
    