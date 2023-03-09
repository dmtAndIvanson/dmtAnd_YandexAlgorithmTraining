def length_between_points(point1, point2):
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2
    
def main():
    # Read file with points.
    finput = open("input.txt", "r")
    size = int(finput.readline().strip())
    coordinates = []
    for _ in range(size):
        coord = tuple(map(float, finput.readline().split()))
        coordinates.append(coord)
    finput.close()

    # Analyze data.
    total = 0
    distances = {}
    for point in range(len(coordinates)):
        for i in range(len(coordinates)):
            length = length_between_points(coordinates[point], coordinates[i])
            if length not in distances:
                distances[length] = 0
            distances[length] += 1
        for key in distances:
            if distances[key] > 1:
                total += distances[key] * (distances[key]-1) // 2
        distances = {}

    # Write answer.
    foutput = open("output.txt", "w")
    foutput.write(f"{total}")
    foutput.close()

main()