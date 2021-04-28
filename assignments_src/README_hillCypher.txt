Casey Richards, cricha97
Intro Python module 11, Hill Cypher

I created a Hill Cypher class so that it could remember objects/values as
attributes rather than needing to call each function individually with parameters.
I stored the input matrices as ndarrays so that matrix math could occur on them.
I chose to save each attribute as a private variable so taht they wouldn't be
modified later by mistake and to practice with data protection.  This created
some suprising bugs as I realized I could not pass these directly into a numpy
function and needed to resave temporarily to pass them (to np.dot() as an
example).  I type checked that all the inputs were in teh correct format and
checked for the inverse within the initialization so that unnecessary
calculations didn't occur.  To calculate the determinant I used the 2x2 formula
with an option for linalg.det() if the matrix wasn't 2X2.  To get the scalar
modular inverse, it was difficult to calculate the negative determinant
as the iterative method did not initially work (as the value always returned a
positive value).  Thus, I modified the given equation using the last anwer to
this: https://math.stackexchange.com/questions/3448234/calculating-modular-multiplicative-inverse-for-negative-values-of-a question as a structure.
To convert the string to integer values and vice versa, I used a dictionary so
that associated values could be quickly and easily accessed without a loop.
To encrypt, if invertible, I converted the string to numeric and used the dot
product of the key matrix and the numeric array as the new values for the string.
To decrypt, the same process was followed with the same key, but this time using
the key's modular inverse to get the reverse values.

There are no known bugs in my program