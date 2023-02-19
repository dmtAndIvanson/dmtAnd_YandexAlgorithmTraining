SIZE = 1000


def read_data(file):
    """Read data from file."""
    a, b = list(map(int, file.readline().split()))

    seq1 = [[] for i in range(SIZE)]
    for i in range(a):
        tmp = int(file.readline())
        seq1[tmp%SIZE].append(tmp)

    seq2 = [[] for i in range(SIZE)]
    for i in range(b):
        tmp = int(file.readline())
        seq2[tmp%SIZE].append(tmp)

    return (seq1, seq2)


def analyze_data(seq1, seq2):
    """Find common elemnts in sequences.
       Return them and sequences without these elements."""
    common = []
    for i in seq1:
        for j in i:
            if j in seq2[j%SIZE]:
                common.append(j)

    for i in common:
        seq1[i%SIZE].remove(i)
        seq2[i%SIZE].remove(i)

    ans1 = []
    for i in seq1:
        ans1 += i

    ans2 = []
    for i in seq2:
        ans2 += i

    return (ans1, ans2, common)


def main():
    # Read data.
    file = open("input.txt", "r")

    seq1, seq2 = read_data(file)

    file.close()

    # Analyze data.
    seq1, seq2, common_seq = analyze_data(seq1, seq2)

    seq1.sort()
    seq2.sort()
    common_seq.sort()

    # Write answer.
    file = open("output.txt", "w")

    line = f"{len(common_seq)}\n{' '.join(map(str, common_seq))}\n{len(seq1)}\n{' '.join(map(str, seq1))}\n{len(seq2)}\n{' '.join(map(str, seq2))}"
    file.write(line)

    file.close()


main()