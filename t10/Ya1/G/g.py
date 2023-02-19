def read_data(file):
    """Read data from file."""
    line = file.readline()
    return list(map(int, line.split()))


def find_details(total, temp, res):
    """Find how many details can be done."""
    details = (total // temp) * (temp // res)

    return details


def main():
    # Read data from file.
    file = open("input.txt", "r")

    total, temp, res = read_data(file)

    file.close()

    # print(total, temp, res)

    details = 0

    # Calculate amount of pieces:
    while (total // temp) > 0:
        temp_details = find_details(total, temp, res)

        total -= temp_details * res

        details += temp_details

    # Read answer to file.
    file = open("output.txt", "w")

    file.write(f"{details}")

    file.close()


main()