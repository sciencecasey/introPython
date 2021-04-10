import math

cluster_changes = 0
clusters = [[], [], [], []]
points = []
prev_cluster_size = [0, 0, 0, 0]  # added, start with empty clusters

# open points.txt for reading points from file
f = open("points.txt", "r")

# read number of clustering iterations from file
iterations = int(f.readline())
# read number of points from file
num_points = int(f.readline())
# read number of clusters from file
num_clusters = int(f.readline())
# read cluster indexes from file
cluster_indexes = []
for i in range(num_clusters):
    cluster_indexes.append(int(f.readline()))

# read and parse points from file into a list
for line in range(num_points):
    point = f.readline().strip().split(',')
    try:
        x = int(point[0])  # input character error here
        y = int(point[1])  # input structure error here
        points.append([x, y])
    except ValueError:  # check for invalid input characters
        print("invalid input, skipping entry: " + str(line))
    except IndexError:  # check for invalid input structure
        print("Indexing error! invalid x,y input.  Skipping entry: " + str(line))
    points.append([x, y])

# select 4 initial centroids
centroids = []
for index in cluster_indexes:
    centroids.append(points[index])

for r in range(iterations):
    for point in points:
        # calculate the distance between the current point and each of the 4 centroids
        d1 = math.sqrt((centroids[0][0] - point[0]) ** 2 + (centroids[0][1] - point[1]) ** 2)
        d2 = math.sqrt((centroids[1][0] - point[0]) ** 2 + (centroids[1][1] - point[1]) ** 2)
        d3 = math.sqrt((centroids[2][0] - point[0]) ** 2 + (centroids[2][1] - point[1]) ** 2)
        d4 = math.sqrt((centroids[3][0] - point[0]) ** 2 + (centroids[3][1] - point[1]) ** 2)

        # assign point to the cluster with the nearest centroid
        if d1 == min(d1, d2, d3, d4):
          # append error, tuple changed to list
          clusters[0].append(point)  # index error, decremented
        elif d2 == min(d1, d2, d3, d4):
          # append error, tuple changed to list
          clusters[1].append(point)  # index error
        elif d3 == min(d1, d2, d3, d4):
          # append error, tuple changed to list
          clusters[2].append(point)  # index err
          # or
        else:
          # append error, tuple changed to list
          clusters[3].append(point)  # index error

    # check if any points have changed clusters
    for i in range(len(clusters)):
        if len(clusters[i]) != prev_cluster_size[i]:
            cluster_changes += cluster_changes

    # calculate the resulting centroid for each cluster using the mean
    for i in range(len(clusters)):
        total_x = 0
        total_y = 0

        # sum the x and y coordinates of each point in the current cluster
        for point in clusters[i]:
            total_x += point[0]
            total_y += point[1]

        # update centroid with the resulting cluster's mean x and y values
        centroids[i][0] = total_x / len(clusters[i])
        centroids[i][1] = total_y / len(clusters[i])

        # store current cluster size for comparison in next iteration
        prev_cluster_size[i] = len(clusters[i])

    # empty the cluster except on final iteration
    if r < iterations:
        for cluster in clusters:
            cluster.clear()

# output number of iterations until clusters are stable
print("Iterations to achieve stability: " + str(cluster_changes))

# output the centroid, the number of points, and a list of points for each cluster
for i in range(len(centroids)):
    print("Centroid " + str(i) + ": " + str(centroids[i]))
    # print("Number of points in Cluster " + str(i) + ": " + str(len(clusters[i]))
    print("Number of points in Cluster " + str(i) + ": " + str(len(clusters[i])))
    print("Cluster " + str(i) + ": " + str(clusters[i]))
