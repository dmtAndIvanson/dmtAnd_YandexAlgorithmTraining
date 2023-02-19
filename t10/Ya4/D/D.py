def read_file(file):
    """Read data from file."""
    ctr1 = int(file.readline())
    seq1 = [0] * ctr1

    line = list(map(int, file.readline().split()))
    for i in range(ctr1):
        seq1[i] = line[i]

    ctr2 = int(file.readline())

    line = list(map(int, file.readline().split()))
    for i in line:
        seq1[i-1] -= 1

    return seq1


def write_answer(file, seq1):
    """Write answer to file."""
    for i in seq1:
        if i < 0:
            file.write("YES\n")
        else:
            file.write("NO\n")


def main():
    # Read data.
    file = open("input.txt", "r")

    # Calculate if button is broken or not.
    btn_state = read_file(file)

    file.close()

    # Write answer.
    file = open("output.txt", "w")

    write_answer(file, btn_state)

    file.close()


main()