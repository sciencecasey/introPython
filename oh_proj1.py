"""
1. Read two integers x,y and print their sum: Sum of <x> + <y> = <sum>
2. Read two integers x,y and print their difference: Difference of <x> - <y> = <difference>
3. Read two floats x,y and print their product: Product of <x> * <y> = <product>
4. Read a single float x and print two things:
4.1) Print the value of x/x
4.2) print the value of x/0
"""

x = input("Give me an integer value: ")
y = input("Give me another integer value: ")
print("The sum of the integers is " + x + " + " + y + " = " + str(int(x) + int(y)))
print("The difference of the integers is " + x + " - " + y + " = " + str(int(x) - int(y)))
print("The product is " + x + " * " + y + " = " + str(int(x) * int(y)))
x = float(input("Tell me a float value: "))
print(str(x/x))
try:
    print(str(x/0))
except ZeroDivisionError:
    print("Error: can't divide by zero!")
