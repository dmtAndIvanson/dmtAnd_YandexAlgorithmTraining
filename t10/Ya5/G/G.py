def fact(num):
    ans = 1
    while num != 1:
        ans *= num
        num -= 1

    return ans


def main():
    # Read data.
    with open("input.txt", "r") as file:
        size, k = list(map(int, file.readline().split()))
        seq1 = list(map(int, file.readline().split()))

    dict1 = {}
    for num in seq1:
        if num not in dict1:
            dict1[num] = 0
        dict1[num] += 1

    total = 0
    
    seq1 = list(dict1.keys())
    seq1.sort()

    # Analyze data.
    for ptr1 in range(len(seq1)):
        ctr1 = 0
        div1 = 1

        ptr2 = ptr1
        while ptr2 < len(seq1):
            # !!! Incorrect condition. Read task carefully.
            if seq1[ptr2] / seq1[ptr1] <= k:
                ctr1 += dict1[seq1[ptr2]]
                div1 *= fact(dict1[seq1[ptr2]])
            ptr2 += 1
        
        if ctr1 >= 3:
            total += (ctr1 * (ctr1-1) * (ctr1-2)) // div1

    # Write answer.
    with open("output.txt", "w") as file:
        file.write(f"{total}")


main()