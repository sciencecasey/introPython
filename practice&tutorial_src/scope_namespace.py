'''
Created on Mar 22, 2021

@author: https://docs.python.org/3.9/tutorial/classes.html
'''

def scope_test():
    def do_local():
        spam = "local spam" # doesn't change the assignment
        
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam" # changes the assignment
        
    def do_global():
        global spam
        spam = "global spam" # changes the assignment at the module level
        
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

if __name__ == '__main__':
    spam = "test spam"
    scope_test()
    print("In global scope:", spam) 