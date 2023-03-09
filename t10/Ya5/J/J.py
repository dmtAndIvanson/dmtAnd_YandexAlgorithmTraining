from math import sqrt
    
def length_between_points(point1, point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    
def main():
    # Read file with points.
    finput = open("input.txt", "r")
    size = int(finput.readline().strip())
    coordinates = []
    for _ in range(size):
        coord = tuple(map(int, finput.readline().split()))
        coordinates.append(coord)
    finput.close()

    total = 0
    distances = {}
    point = 0
    """
    while point < len(coordinates):
        for i in range(len(coordinates)):
            if point+i < len(coordinates):
                length = length_between_points(coordinates[point], coordinates[point+i])
                print(i, coordinates[point],coordinates[point+i], length)
                if length not in distances:
                    distances[length] = 0
                distances[length] += 1
    """
    while point < len(coordinates):
        for i in range(len(coordinates)):
            #if point+i < len(coordinates):
            length = length_between_points(coordinates[point], coordinates[i])
            #print(i, coordinates[point],coordinates[i], length)
            if length not in distances:
                distances[length] = 0
            distances[length] += 1
        #print(distances)
        for key in distances:
            if distances[key] > 1:
                total += distances[key] * (distances[key]-1) / 2
        distances = {}
        point += 1
    #print(total)

    # Write answer.
    foutput = open("output.txt", "w")

    foutput.write(f"{total}")

    foutput.close()

main()