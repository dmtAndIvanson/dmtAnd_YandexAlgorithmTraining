def find_answer(file):
    """Find close in meaning word."""
    dict1 = {}

    # Read words and append to dictionary.
    ctr = int(file.readline())
    for i in range(ctr):
        j, k = file.readline().split()
        dict1[j] = k
        dict1[k] = j

    # Find word close in meaning.
    word = file.readline().strip()
    ans = dict1[word]

    return ans


def main():
    # Find answer.
    file = open("input.txt", "r")

    ans = find_answer(file)

    file.close()
    
    # Write answer.
    file = open("output.txt", "w")

    file.write(ans)

    file.close()


main()