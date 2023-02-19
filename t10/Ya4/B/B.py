def count_repeat(file):
    """Count how many times word have been in text."""
    dict1 = {}
    list1 = []

    line = file.readline()
    while line != "":
        line = line.split()
        for i in line:
            if i not in dict1:
                dict1[i] = 0
            list1.append(dict1[i])
            dict1[i] += 1
        line = file.readline()

    ans = ' '.join(map(str, list1))

    return ans


def main():
    # Find answer.
    file = open("input.txt", "r")

    ans = count_repeat(file)

    file.close()

    # Write answer.
    file = open("output.txt", "w")

    file.write(ans)

    file.close()


main()