Casey Richards, cricha87 
Intro Python week 6 Homework
Catalan numbers & Pascal's triangle

The Catalan Numbers script uses a single, recursive function to solve the catalan number problem.  A if __name__ == "__main__" calls this function within a for loop to return the desired values. I used the floor() function in order to return a whole number and always round down, as is necessary for the sequence to come out correctly.  Catalan uses an inner function to evaluate the recursion and make parameter passing and ease of use simple from the external perspective. 

The Pascal script has a couple options for calling pascal, one iterative and the other recursive.  The recursive function uses an inner function as a helper method so that more parameter values can be passed silently, keeping use very simple from the outside.  I stored the triangle the same way in both methods, in a list of nested lists.  The functions both check if at the start or end of a row, automatically adding a 1 in those cases or using the previous item in the overall triangle list (which is the previous row) and checking the addition of the value with the same index, and one index less than our target location on the current row.  In order to print the recursive triangle all at once, I created a print_tri() method to facilitate easy printing.  Although I could've written this within main, I wrote it as it's own function so that it could be reused if desired. 

There are no known bugs in my scripts
