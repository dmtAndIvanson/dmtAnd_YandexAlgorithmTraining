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
    for d1 in range(size):
        for d2 in range(d1+1,size):
            for d3 in range(d2+1,size):
                length1 = (coordinates[d1][0]-coordinates[d2][0])**2 + (coordinates[d1][1]-coordinates[d2][1])**2
                length2 = (coordinates[d1][0]-coordinates[d3][0])**2 + (coordinates[d1][1]-coordinates[d3][1])**2
                length3 = (coordinates[d2][0]-coordinates[d3][0])**2 + (coordinates[d2][1]-coordinates[d3][1])**2
                # Не учтено, что точки могут быть на одной прямой.
                if length1 == length2 or length1 == length3 or length2 == length3:
                    total += 1

    # Write answer.
    foutput = open("output.txt", "w")
    foutput.write(f"{int(total)}")
    foutput.close()

main()