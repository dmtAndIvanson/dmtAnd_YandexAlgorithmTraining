def main():
    # Read data from file.
    finput = open("input.txt", "r")
    cr_count = int(finput.readline().strip())

    # Fill list with power of conditioner for each class.
    cr_list = [0]*cr_count
    ctr = 0
    for cr in map(int, finput.readline().split()):
        cr_list[ctr] = cr
        ctr += 1

    cond_count = int(finput.readline().strip())

    # Fill dictionary with {power: price} pairs.
    cond_dict = {}
    power_list = []
    for i in range(0, cond_count):
        power, price = tuple(map(int, finput.readline().split()))
        if power not in cond_dict: # Create pair.
            cond_dict[power] = price
            power_list.append(power)
        elif cond_dict[power] > price: # Update value.
            cond_dict[power] = price

    finput.close()

    #print(cr_count, "-", cr_list)
    #print(cond_count, "-", power_list, "-", cond_dict)

    # Analyze data.
    # Sort list of classrooms and power.
    cr_list.sort()
    power_list.sort()

    # In power list skip conditioner,
    # if it's power less and price greater
    # than price for conditioner with greater power.
    left = 0
    right = len(power_list)-1
    new_left = 0 
    while left < right:
        if cond_dict[power_list[left]] > cond_dict[power_list[left+1]]:
            new_left = left+1
        left += 1
    power_list = power_list[new_left:]

    # Find total price.
    cr_ctr = 0
    pwr_ctr = 0
    price = 0
    while cr_ctr < len(cr_list) and pwr_ctr < len(power_list):
        if power_list[pwr_ctr] >= cr_list[cr_ctr]:
            price += cond_dict[power_list[pwr_ctr]]
            cr_ctr += 1
        else:
            pwr_ctr += 1

    #print(cr_count, "-", cr_list)
    #print(cond_count, "-", power_list, "-", cond_dict)
    print(price)

    foutput = open("output.txt", "w")
    foutput.write(f"{price}")
    foutput.close()

main()