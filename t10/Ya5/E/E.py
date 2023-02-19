def find_shortest_seq(seq, total):
    """Find the shortest subsequence of the sequence,
       that contains all possible elements."""
    left = 1
    right = len(seq)
    min_len = right - left + 1

    for i in range(len(seq)):
        tmp_el = set()
        tmp_len = 0

        for j in range(i, len(seq)):
            tmp_len += 1
            
            if seq[j] not in tmp_el:
                tmp_el.add(seq[j])

            if tmp_len >= min_len:
                break

            elif  len(tmp_el) == total:
                min_len = tmp_len
                left = i + 1
                right = j + 1

    return (left, right)


def main():
    # Read data.
    with open("input.txt", "r") as file:
        length, total = list(map(int, file.readline().split()))

        seq = list(map(int, file.readline().split()))

    # Analyze data.
    l, r = find_shortest_seq(seq, total)

    # Write answer.
    with open("output.txt", "w") as file:
        file.write(f"{l} {r}")


main()