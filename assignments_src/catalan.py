'''
Created on Mar 2, 2021
Catalan numbers using nested functions and call to main
@author: CaseyJayne
'''
from gmpy2 import floor


def catalan(n: int) -> int:
    """
    @param n: the desired order of catalan numbers
    @return: the catalan number of the n-th order  
    """
    if n in (0, 1):
        return 1

    def real_catalan(k, n):
        if k == n:
            # base case
            return (n + k) / k  # take the floor
        if k < n:
            # print(f"K is {k} \n N is {n}")
            return ((n + k) / k) * real_catalan(k + 1, n)

    return floor(real_catalan(2, n))


def main():
    for i in range(2, 16):
        print("Order " + str(i) + " Catalan number is " + str(catalan(i)))


if __name__ == '__main__':
    main()
