def read_data(file):
    """Read data from file."""
    size = int(file.readline())

    seq = list(map(int, file.readline().split()))

    number = int(file.readline())

    return (size, seq, number)


def find_near_num(size, seq, number):
    """Find the closest to number number2 in sequence.
       If there is two numbers, returns both."""

    l_num = seq[0] # Closest number that less than number.
    r_num = seq[0] # Closest number that more than number.

    for i in range(1, size):
        if seq[i] == number:
            return (number,)

        elif abs(number - seq[i]) < abs(number - l_num):
            l_num = seq[i]
            r_num = seq[i]

        elif abs(number - seq[i]) == abs(number - l_num):
            if l_num == r_num:
                if seq[i] < number:
                    l_num = seq[i]
                else:
                    r_num = seq[i]

    if l_num == r_num:
        return (l_num,)

    else:
        return (l_num, r_num)


def write_answer(file, ans):
    """Write answer to file."""
    file.write(ans)


def main():
    # Read data from file.
    file = open("input.txt", "r")

    size, seq, number = read_data(file)

    file.close()

    # Determine type of sequence.
    res = find_near_num(size, seq, number)

    ans = str(res[0])

    # Write answer.
    file = open("output.txt", "w")

    write_answer(file, ans)

    file.close()


main()