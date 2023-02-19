def main():
    # Read data.
    with open("input.txt", "r") as fin:
        total, val = list(map(int, fin.readline().split()))
        seq1 = list(map(int, fin.readline().split()))
    
    ctr1 = 0 # Counter.
    ps = 0   # Prefix sum.

    # Make dictionary of prefixsum (PS) starting with 0.
    ps_dict = {0: 1, }
    for num in seq1:
        ps += num

        # If next PS is not in dictionary - create it.
        if ps not in ps_dict:
            ps_dict[ps] = 0
        ps_dict[ps] += 1

        # If (PS-17) is in dictionary count it.
        if ps-val in ps_dict:
            ctr1 += 1

    # Write answer.
    with open("output.txt", "w") as fout:
        fout.write(f"{ctr1}")


main()