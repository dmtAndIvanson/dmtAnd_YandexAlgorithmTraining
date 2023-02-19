def main():
    # Read data.
    file = open("input.txt", "r")

    line = file.readline().split()
    list1 = list(map(int, line))

    line = file.readline().strip('\n')
    list2 = [int(i) for i in line]

    file.close()

    # Analyze data.
    seq = [0 for i in range(10)]

    for i in list1:
        seq[i] = -1

    sum1 = 0
    for i in list2:
        if seq[i] == 0:
            seq[i] += 1
            sum1 += 1

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{sum1}")

    file.close()


main()
