""" Homework 2 Intro Python
Casey Richards
"""

principle = input("Please enter the principle amount: ")
rate = input("Please enter the interest rate: ")
if float(rate) > 1:
    # inserted as percent, change to decimal
    rate = float(rate) / 100

term = input("Please enter the loan period in years: ")
per_year = input("Please enter the payments per year: ")
exp = int(per_year)*int(term)
frac: float = 1 + float(rate)/int(per_year)
amt = float(principle) * (frac**exp)

print("Total paid after " + term + " years: $%.2f" % amt + ", where " + term + " is the term "/
      "of the loan and \n$%.2f" % (amt - int(principle)) + " is the total interest paid on the loan.")
