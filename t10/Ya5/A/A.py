# Slow solution.
def main():
    # Read data.
    with open("input.txt", "r") as fin:
        fin.readline()
        seq1 = list(map(int, fin.readline().split()))
        fin.readline()
        seq2 = list(map(int, fin.readline().split()))

    # Find pair with lowest difference.
    min_pair = tuple()
    min_dif = float("inf")

    for i in seq1:
        for j in seq2:
            if abs(i-j) < min_dif:
                min_dif = abs(i-j)
                min_pair = (i,j) 

    # Write answer.
    with open("output.txt", "w") as fout:
        fout.write(f"{min_pair[0]} {min_pair[1]}")


main()