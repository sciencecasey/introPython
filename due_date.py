"""Assignment 1 Casey Richards
Print the assignment due date
"""
#  prompt user for day, month, year, time (hours), and time(minutes)
year = input("Please type the current year: ")
print(type(year))
month = input("Please type the numeric month: ")
day = input("Please type the numeric day of the month: ")
hour = input("Please type the two-digit hour: ")
minute = input("Please type the two-digit minute past the hour: ")
print("\nThanks!")

#print the input
print("\nModule 1 assignment is due on " + month + "/" + day + "/" + year + " at "\
      + hour + ":" + minute + " EST.\n")
