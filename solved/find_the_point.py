num_points = int(input())

for i in range(num_points):
    points = [int(x) for x in input().split(" ")]
    p1 = points[:2]
    p2 = points[2:]

    dist = [p2[0] - p1[0], p2[1] - p1[1]]
    p3 = [p2[0] + dist[0], p2[1] + dist[1]]

    print(str(p3[0]) + " " + str(p3[1]))