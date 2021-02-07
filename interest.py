""" Homework 2 Intro Python
Casey Richards
"""
# p = 625937
# r = .035
# t = 30
# n = 12
p = input("Please enter the principle amount: ")
r = input("Please enter the interest rate: ")
if float(r) > 1:
    # inserted as percent, change to decimal
    r = float(r) / 100

t = input("Please enter the loan period in years: ")
n = input("Please enter the payments per year: ")
exp = int(n)*int(t)
frac: float = 1 + float(r)/int(n)
a = float(p) * (frac**exp)

print("Total paid after " + t + " years: $%.2f" % a + ", where " + t + " is the term "/
      "of the loan and \n$%.2f" % (a - int(p)) + " is the total interest paid on the loan.")
