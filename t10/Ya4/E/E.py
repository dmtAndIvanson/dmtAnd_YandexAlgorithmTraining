def make_dict(file):
    """Read data from file."""
    dict1 = {}

    ctr1 = int(file.readline())
    for i in range(ctr1):
        a, b = list(map(int, file.readline().split()))

        if a not in dict1:
            dict1[a] = []
        dict1[a].append(b)

    return dict1


def main():
    # Read data.
    file = open("input.txt", "r")

    width_dict = make_dict(file)

    file.close()

    # Analyze data.
    for i in width_dict:
        width_dict[i].sort(reverse=True)

    # Make pyramid.
    # Sort width values.
    all_width = [i for i in width_dict]
    all_width.sort(reverse=True)

    # In descending order calculate sum of maximum heights.
    height = 0
    for i in all_width:
        height += width_dict[i][0]

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{height}")

    file.close()


main()