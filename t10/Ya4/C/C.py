def find_answer(file):
    """Find most repeated word."""
    dict1 = {}
    word = ''
    w_count = 0

    line = file.readline()
    while(line != ''):
        line = line.split()
        for i in line:
            if i not in dict1:
                dict1[i] = 0
            dict1[i] += 1

            if dict1[i] > w_count:
                word = i
                w_count = dict1[i]
            elif dict1[i] == w_count and i < word:
                word = i

        line = file.readline()

    return word


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