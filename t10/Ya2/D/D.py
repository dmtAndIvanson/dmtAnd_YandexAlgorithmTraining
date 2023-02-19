def read_data(file):
    """Read sequence from file."""
    line = file.readline()

    seq = list(map(int, line.split()))

    return seq


def count_supremum(seq):
    """Count how many digits in sequense more than its neighbors."""
    if len(seq) < 3:
        return 0

    ctr = 0
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] and seq[i+1] > seq[i+2]:
            ctr += 1

    return ctr


def main():
    # Read data.
    file = open("input.txt", "r")

    seq = read_data(file)

    file.close()

    # Analyse data.
    ans = count_supremum(seq)

    # Write answer.
    file = open("output.txt", "w")

    file.write(str(ans))

    file.close()


main()