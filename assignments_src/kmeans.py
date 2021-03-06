"""
Module 5, Intro to Python
K-means Clustering assignment
statistical method for coronavirus and likelihood of being infected via an infected person
Casey Richards
"""
with open("kmeans.txt") as file:
    max_iter = int(file.readline().strip())
    num_points = int(file.readline().strip())
    num_clusters = int(file.readline().strip())
    num_kmeans = 0

    # make a list of lists containing center-points
    centers = []
    for line in range(num_clusters):
        index = int(file.readline().strip())
        centers.append(index)  # add to list

    # order the list of centers
    centers.sort()

    # make a list of lists to hold the groups
    groups = []
    for number in range(num_clusters):
        groups.append([])

    # read in the points and place into general or center list
    all_points = []
    center_ind = 0
    for line in file:
        points = line.strip()  # a string
        x, y = points.split(",")  # list of strings
        x = int(x)
        y = int(y)
        if center_ind >= num_clusters:
            # will go here after finishing adding the center points
            all_points.append((x, y))
        elif len(all_points) == centers[center_ind]:
            # this is the center point!
            centers[center_ind] = (x, y)
            center_ind += 1
        else:
            all_points.append((x, y))
    # exit block to close file

# Calculate the initial groups and place points into the groups
for points in all_points:
    dist = -1
    group = -1
    center_ind = 0
    for center in centers:
        # get euclidian distance
        tempdist = ((points[0] - center[0])**2 + (points[1] - center[1])**2)**(1/2)
        if dist == -1:
            # first distance is the closest
            dist = tempdist
            group = 0  # first group is the zero index
            center_ind += 1
        elif tempdist > dist:
            # don't need to change to new distance
            center_ind += 1
        else:
            dist = tempdist
            group = center_ind
            center_ind += 1# the number of the group

    # place the point in the group it was assigned, by the closest distance
    groups[group].append(points)

# add centers to initial groups and then start kmeans!
# a post from Joe said we don't need to do this
# groups[0].append(centers[0])
# groups[1].append(centers[1])
# groups[2].append(centers[2])
# groups[3].append(centers[3])

num_moved = 0
kmean = True
while kmean:
    num_kmeans += 1
    # orig_len0 = len(groups[0])
    # orig_len1 = len(groups[1])
    # orig_len2 = len(groups[2])
    # orig_len3 = len(groups[3])
    for index in range(4):
        x = 0
        y = 0
        for item in groups[index]:
            x += item[0]
            y += item[1]
        avgX, avgY = (x/len(groups[index]), y/len(groups[index]))
        centers[index] = (avgX, avgY) # add the centers to calculate distances

    for orig_group in range(4):
        for points in groups[orig_group]: # points is a tuple, groups is a list
            # start with the distance of the home group
            dist = -1
            group_num = -1
            center_ind = 0
            for center in centers: # center is a tuple, centers is a list
                # get euclidian distance
                tempdist = ((points[0] - center[0]) ** 2 + (points[1] - center[1]) ** 2) ** (1 / 2)
                if dist == -1:
                    # first distance is the closest
                    dist = tempdist
                    group_num = 0  # first group is the zero index
                    center_ind += 1
                elif tempdist > dist:
                    # don't need to change to new distance
                    center_ind += 1
                else:
                    # temp dist shorter - move to this group
                    dist = tempdist
                    group_num = center_ind # the number of the group
                    center_ind += 1

            # check if there needs to be a change
            if orig_group != group_num:
                # need to switch
                num_moved += 1
                groups[group_num].append(points) # add to new group
                groups[orig_group].remove(points) # take off original list
    # after_len0 = len(groups[0])
    # after_len1 = len(groups[1])
    # after_len2 = len(groups[2])
    # after_len3 = len(groups[3])

    # used below with measuring with length rather than number moved
    # if (after_len1 == orig_len1) and (after_len0 == orig_len0) and \
    #        (after_len2 == orig_len2 ) and (after_len3 == orig_len3):
    if num_moved == 0 or max_iter <= num_kmeans:  # originally used this metric
        # nothing moved, done with means!
        kmean = False
    else:
        # reset the move number
        num_moved = 0


print(f"The number of kmeans: {num_kmeans}\n"
      f"Centroid 0: {centers[0]}\n"
      f"number of items in Cluster 0: {len(groups[0])}\n"
      f"Cluster 0: {groups[0]}\n"
      f"number of items in Cluster 1: {len(groups[1])}\n"
      f"Cluster 1: {groups[1]}\n"
      f"number of items in Cluster 2: {len(groups[2])}\n"
      f"Cluster 2: {groups[2]}\n"
      f"number of items in Cluster 3: {len(groups[3])}\n"
      f"Cluster 3: {groups[3]}"
      )