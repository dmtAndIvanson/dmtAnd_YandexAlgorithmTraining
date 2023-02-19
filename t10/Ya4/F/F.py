def read_data(file):
    """Read data from file."""
    dict1 = {}
    
    line = file.readline()
    while line != "":
        surname, item, count = line.split()
        count = int(count)

        if surname not in dict1:
            dict1[surname] = {}
        if item not in dict1[surname]:
            dict1[surname][item] = 0
        dict1[surname][item] += count

        line = file.readline()

    return dict1


def write_answer(file, dict1):
    """Write answer."""
    for name in dict1:
        file.write(name + ":\n")

        # Sort items.
        seq1 = sort_keys(dict1[name])
        for item in seq1:
            file.write(f"{item} {dict1[name][item]}\n")


def sort_keys(dict1):
    """Return sorted list of keys."""
    seq = []
    for i in dict1:
        seq.append(i)

    seq.sort()

    return seq


def main():
    # Read data to dictionary {Surname: {Item: Count}}.
    file = open("input.txt", "r")

    dict1 = read_data(file)

    file.close()

    # Write answer.
    file = open("output.txt", "w")

    write_answer(file, dict1)

    file.close()


main()