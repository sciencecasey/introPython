"""
1. Open points.txt and create a list of tuples where each tuple is a pair of floating point numbers (x, y).  You may
find the strip() and split() string methods useful here

2. Add 1.0 to the x-coordinate of each point in your list.

3. Compute the slope between the first point and all other points.  As you do, print each slope and add it to a set to
keep track of the number of unique slopes that will be calculated.
Additionally, keep track of the maximum slope value for the 4 slopes being computed.

4. Once all slopes have been calculated, print the following 2 outputs:
4a. "Max. slope: M", where M is the maximum slope value computed
4b. "There were N distinct slopes: S", where N is the number of distinct slopes and S is the set containing those slopes.

"""
"""
file = open("/Users/CaseyJayne/Downloads/points.txt", "r")

temp = []
for line in file.readlines():
    temp.append(line.rstrip("\n"))

listy = []
tup = ()
for item in temp:
    x, y = item.split(",")
    tup = (float(x), float(y))
    listy.append(tup)http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=9295

print(listy)
print(type(listy))
print(type(listy[0]))

file.close()
"""

########### better!
file = open("/Users/CaseyJayne/Downloads/points.txt", "r")
temp = []
for line in file.readlines():
    point = (line.rstrip("\n")).split(",")
    temp.append((float(point[0]), float(point[1])))

for item in range(len(temp)):
    temp[item] = (temp[item][0]+1, temp[item][1])

sety = set()
maxy = 0
for i in range(1, len(temp)):
    m = (temp[0][1] - temp[i][1])/([temp][0][0] - temp[i][0])
    sety.add(m)
    if abs(m) > max:
        maxy = abs(m)

print("There were " + str(len(sety)) + " distinct slopes, the max of which was: " + str(maxy))
file.close()



