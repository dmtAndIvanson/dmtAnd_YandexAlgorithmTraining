def main():
    # Read data.
    with open("input.txt", "r") as file:
        file.readline()
        cl_rm = list(map(int, file.readline().split()))

        ctr1 = int(file.readline())
        wlt_prc = dict()
        # Make dictionary {walt: price}.
        for i in range(ctr1):
            walt, price = tuple(map(int, file.readline().split()))

            if walt not in wlt_prc:
                wlt_prc[walt] = price
            # If new price less than old, update it.
            elif wlt_prc[walt] > price:
                wlt_prc[walt] = price
    
    # Analyze data.
    # Sort keys of dictionary in descending order.
    k_list = list(wlt_prc.keys())
    k_list.sort(reverse=True)

    # Add key to new list, if price of new item is less than for previous.
    nk_list = [k_list[0]]
    for i in range(1,len(k_list)):
        val = k_list[i]
        tmp = nk_list[-1]

        if wlt_prc[val] < wlt_prc[tmp]:
            nk_list.append(val)


    # Create dictionary {model: [classroom,]}.
    #mdl_clr = dict()

    # Count total price.
    total = 0

    ctr2 = len(nk_list) - 1
    for clr in cl_rm:
        while nk_list[ctr2] < clr and ctr2 >= 0:
            ctr2 -= 1
        
        if ctr2 < 0:
            break
        #elif nk_list[ctr2] not in mdl_clr:
        #   mdl_clr[nk_list[ctr2]] = []

        #mdl_clr[nk_list[ctr2]].append(clr)
        else:
            total += wlt_prc[nk_list[ctr2]]

    # Write answer.
    with open("output.txt", "w") as file:
        file.write(f"{total}")
    

main()