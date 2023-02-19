def read_data(file):
    """Read data from file. *File should contain sequence of numbers."""
    line = file.readline()

    seq = list(map(int, line.split()))

    return seq


def is_seq_grows(seq):
    """Return True if sequense grows. False otherwise."""
    if len(seq) < 1:
        return False
    elif len(seq) == 1:
        return True

    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return False

    return True


def write_ans(file, ans):
    """Write answer to file."""
    if ans == True:
        file.write("YES")
    else:
        file.write("NO")


def main():
    # Open input file
    file = open("input.txt", "r")

    # Read data
    seq = read_data(file)

    file.close()

    # Analyse whether the sequence grows
    ans = is_seq_grows(seq)

    # Write answer to output file
    file = open("output.txt", "w")

    write_ans(file, ans)

    file.close()


main()