""" Homework 2
Casey Richards
Use formula to calculate interest rate given total amount paid, pricipal amt, term,
and number of payments
"""

total = input("Please enter the total amount paid: ")
principle = input("Please enter the principle amount: ")
left = float(total)/float(principle)
term = input("Please enter the loan period in years: ")
per_year = input("Please enter the payments per year: ")
exp = 1/(float(per_year)*float(term))
rate = (left**exp - 1)*1000

print("If the total paid was : " + total + " over " + term + " years. At " + per_year +
      " payments per year,\n for the principle amount " + principle + ", the interest rate "
      "was " + str(rate) + "%")

# alternative formula - not solved by algebra as above was off by a factor of 10
# interest = float(total) - float(principle)
# rate = interest**exp - 1
# print("Or perhaps " + str(rate))
