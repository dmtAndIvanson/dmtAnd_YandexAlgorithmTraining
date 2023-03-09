def main():
    # Read data from file.
    finput = open("input.txt", "r")
    n, k = list(map(int, finput.readline().split()))
    # Values of cards store in dictionary {value: count}.
    x_count = {}
    # Also make list of unique values. Sort that list.
    x_list = []
    for x in map(int, finput.readline().split()):
        if x not in x_count:
            x_list.append(x)
            x_count[x] = 0
        x_count[x] += 1
    finput.close()
    x_list.sort()
    print(x_list, "-", x_count)

    # Analyze intervals of three cards.
    # Check that division of third number to the first less or equal to k.
    ctr = 0
    total = 0
    while ctr < len(x_list)-2:
        if x_list[ctr] / x_list[ctr+2] <= k:
            tmp_sum = x_list[ctr] + x_list[ctr+1] + x_list[ctr+2]
            total += tmp_sum * (tmp_sum-1) * (tmp_sum-2)
        ctr += 1
    
    print(total)

main()