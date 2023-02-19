# Fast solution.
def find_min_dif(seq1, seq2):
    """Find the lowest difference between numnbers in sorted sequence."""
    state = 0
    if len(seq1) < len(seq2):
        seq1, seq2 = seq2, seq1
        state = 1

    # Make pointers to elements in two sequences.
    ptr1 = 0
    ptr2 = 0

    min_dif = abs(seq1[0] - seq2[0])
    min_pair = (seq1[0], seq2[0])

    while (ptr1 < len(seq1) - 1) and ptr2 < len(seq2):
        dif1 = abs(seq1[ptr1] - seq2[ptr2])
        dif2 = abs(seq1[ptr1+1] - seq2[ptr2])

        # Update lowest difference if should.
        if dif1 < min_dif:
            min_dif = abs(seq1[ptr1] - seq2[ptr2])
            min_pair = (seq1[ptr1], seq2[ptr2])
        elif dif2 < min_dif:
            min_dif = abs(seq1[ptr1+1] - seq2[ptr2])
            min_pair = (seq1[ptr1+1], seq2[ptr2])

        # Update pointers.
        if dif1 >= dif2:
            ptr1 += 1
        else:
            ptr2 += 1

    return min_pair if state == 0 else (min_pair[1], min_pair[0])
    


def main():
    # Read data.
    with open("input.txt", "r") as fin:
        fin.readline()
        seq1 = list(map(int, fin.readline().split()))
        fin.readline()
        seq2 = list(map(int, fin.readline().split()))

    # Find answer.

    ans1, ans2 = find_min_dif(seq1, seq2)

    # Write answer.
    #print(f"{ans1} {ans2}")
    with open("output.txt", "w") as fout:
        fout.write(f"{ans1} {ans2}")


main()