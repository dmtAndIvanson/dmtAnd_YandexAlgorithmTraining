SIZE = 100


def find_intersec(seq1, seq2): # Work slow.
    """Find common elements in two hash tables."""
    intersec = []
    for i in seq1:
        for j in i:
            if j in seq2[j % SIZE]:
                intersec.append(j)

    intersec.sort()

    ans = ' '.join(map(str, intersec))

    return ans


def main():
    # Read data.
    file = open("input.txt", "r")

    line1 = file.readline().split()
    line2 = file.readline().split()

    file.close()

    # Make hash table.
    seq1 = [[] for i in range(SIZE)]
    seq2 = [[] for i in range(SIZE)]

    for i in line1:
        i = int(i)
        index = i % SIZE
        seq1[index].append(i)

    for i in line2:
        i = int(i)
        index = i % SIZE
        seq2[index].append(i)

    # Analyze data.
    ans = find_intersec(seq1, seq2)

    # Write answer.
    file = open("output.txt", "w")

    file.write(ans)

    file.close()


main()