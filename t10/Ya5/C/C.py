def main():
    # Read data.
    fin = open("input.txt", "r")

    ctr1 = int(fin.readline().strip())
    
    # Start count prefixsum.
    x1, y1 = list(map(int, fin.readline().split()))

    ps_up = y1
    ps_dn = y1
    ps_list = [(0,0), (ps_up,ps_dn)] # List for prefixsum.

    for i in range(ctr1-1):
        x2, y2 = list(map(int, fin.readline().split()))
        
        if y2 > y1:
            ps_up += abs(y2 - y1)
        else:
            ps_dn += abs(y2 - y1)
        
        ps_list.append((ps_up,ps_dn))
        y1 = y2
    
    # Analyze data.
    ctr2 = int(fin.readline().strip())
    ans = []

    for i in range(ctr2):
        l,r = list(map(int, fin.readline().split()))
        
        val = 0
        if l < r:
            val = ps_list[r][0] - ps_list[l][0]
        else:
            val = ps_list[l][1] - ps_list[r][1]

        ans.append(val)

    fin.close()

    # Write answer.
    with open("output.txt", "w") as fout:
        for i in ans:
            fout.write(f"{i}\n")


main()