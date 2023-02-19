# Works but demands a lot of memory.

def main():
    # Read data.
    with open("input.txt", "r") as file:
        m_count, min_dist = list(map(int, file.readline().split()))
        dist_seq = list(map(int, file.readline().split()))

        dist1 = dist_seq.pop(0)

        # Count prefixsum for disstance between monuments.
        ps = 0
        ps_list = [0,]
        while len(dist_seq) != 0:
            dist2 = dist_seq.pop(0)
            ps += (dist2 - dist1)
            ps_list.append(ps)
            dist1 = dist2

    del dist_seq
    # Analyze data.
    # Find distance between monuments, that bigger than min_dist and count possible pairs.
    pos_pair = 0

    ptr1 = 0
    ptr2 = 1
    while ptr1 < len(ps_list) - 1:
        # If PS greaner than min_dist count possible pairs.
        if ps_list[ptr2] - ps_list[ptr1] > min_dist:
            pos_pair += len(ps_list) - ptr2
            #print(ps_list[ptr2] - ps_list[ptr1], '---', ptr1, ptr2)
            ptr1 += 1
            ptr2 = ptr1 + 1
        # If distance to the last monument less than min_dist, stop iteration.
        elif ps_list[-1] - ps_list[ptr1] < min_dist:
            break
        # Else update right monument.
        else:
            ptr2 += 1
            if ptr2 == len(ps_list):
                ptr1 += 1
                ptr2 = ptr1 + 1 

    # Write answer.
    with open("output.txt", "w") as file:
        file.write(f"{pos_pair}")

        
main()