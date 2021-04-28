'''
Created on Mar 2, 2021

@author: CaseyJayne
'''

def no_list(param = ["####"]):
    return param

def f(my_list=None):
    if my_list is None:
        my_list = []
        my_list.append('###')
    return my_list


def avg(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

if __name__ == '__main__':
    print("main program")
    print(f())
    print(f())
    print(f())
    print(no_list())
    print(no_list(param = "hey"))