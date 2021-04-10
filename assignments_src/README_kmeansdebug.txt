Casey Richards, cricha87
Intro to Python - kmeans debugging module 10


1. The first bug was lexical in nature as there was an unmatched closing parenthesis in the definition of clusters().  I fixed this bug by deleting the parenthesis
2. There was a lexical error incrementing clusters on line 61.  I fixed this by using cluster_changes "+= 1" rather than "++"
3. There was an unmatched closing bracket (lexical error) on line 92 which I fixed by adding the closing bracket at the end of the print statement.
4. There was a semantic error in the point input.  I found this error using python debugger.  First I created a logical statement to enter a breakpoint everytime line % 10 == 0 so I could find out how far into the process it was occuring.  This showed the error occured between 20th and 30th input. I then stepped through with next until either point had a value of 40. First I investigated the type and then checked if int(point[0/1]) returned an error without going to that portion of the code.  When I continued to the line x = int(point[0]) when line == 27, I got a ValueError that '4O' was invalid for base 10. I realized that what looked like a zero was actually an 'o'.  Thus, I added a try except statment to check that input could be converted to an integer and if not, the input was skipped.
5. There was a semantic indexing error where a point was out of index range (in the same codeblock).  Thus, I added an except statment to catch IndexErrors as well and skipping them if there was no point[0] or point[1].
6. There was a stylistic error in the code indentation as the indentations were not multiples of 4, thus I used Pycharm to reformat the entire file.
7. There was a logical (or potential logical) error that the file f was never closed.  Although it did not cause issues in this case, it could and acted as a resource leak. I fixed this error by adding the line f.close().
8. There was no check that the path to the file was correct, so I added a Try, Except, else statement to exit the program early if the file wasn't found.
9. There was a logical error in the math equations as the correct equation needs to square the entire value of the centroid - point but as it was, only the point was squared.  To fix this I added parenthesis around centroid - point portions of the equations.
10 - 13. There was a syntax error when we attempted to append the minimum distance to a cluster.  This can't occur as tuples are immutable, thus I changed cluster from a list of tuples to a list of lists.
14 - 17. There was a semantic error in the indexing of the clusters as indeces were attempted with a 1 index rather than 0.  I reduced each cluster value by 1 to achieve the correct python indeces.
18. There was a syntax error in the reference to prev_cluster_size as the variable was not initialized yet and couldn't be accessed.  To fix this I needed to add a prev_cluster_size[] values in the initialization to 0.
19. There was a logical error in that there was no check to see if the size of the clusters changed to break out of the number of kmeans passes.  I added a prev_changed value and a break out if prev_changes == cluster_changes.
20. There was an unmatched opening bracket in the print statments that I added to make it lexically correct.
21. There was a logical error in that the cluster_changes was printed as the iterations although iterations were different.  I added a line changing the iterations equal to r (which counted the times we looped) and added a print statement for that.

