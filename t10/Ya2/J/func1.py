def find_corners(values, first_val):
    """Find corners, where unknown value should be.
       Use data in values to find it."""
    left = 30.0
    right = 4000.0

    val = first_val

    for i in values:
        if i[0] < val:
            if i[1] == 'further':
                temp = (i[0] + val) / 2

                if temp > left:
                    left = temp

            elif i[1] == 'closer':
                temp = (i[0] + val) / 2
                
                if temp < right:
                    right = temp

        elif i[0] > val:
            if i[1] == 'further':
                temp = (val + i[0]) / 2

                if temp < right:
                    right = temp

            elif i[1] == 'closer':
                temp = (val + i[0]) / 2

                if temp > left:
                    left = temp

        val = i[0]

    return (left, right)
       
       
def read_data(file):
    """Read data from file."""
    count = int(file.readline()) - 1

    val = int(file.readline())

    values = []

    for i in range(count):
        a, b = file.readline().split()

        values.append((int(a), b))

    return (val, values)


def main():
    # Read data from file.
    file = open("input.txt", "r")

    val, values = read_data(file)

    file.close()

    # Analyze data.
    left, right = find_corners(values, val)

    # Round values.
    round(left, 6)
    round(right, 6)

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{left} {right}")

    file.close()


main()