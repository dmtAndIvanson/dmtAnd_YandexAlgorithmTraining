# Solution with two pointers.

def find_shortest_seq(seq, unique_count):
    """Find shortest unseparated sequnce with all unique elements."""
    min_size = len(seq)
    min_left = 1
    min_right = len(seq)
    left = right = 0 # Set 2 pointers.

    # Declare variables for count.
    tmp_size = 0
    sort_in_seq = {} # To check how many sorts in seqence.

    while right <= len(seq) and left <= right:
        # Break loop if bad conditions.
        if right >= len(seq) and len(sort_in_seq) < unique_count:
            right += 1
            unique_count = -1
        if len(sort_in_seq) < unique_count:
            if seq[right] not in sort_in_seq:
                sort_in_seq[seq[right]] = 0
            sort_in_seq[seq[right]] += 1
            tmp_size += 1
            right += 1 # Update pointer.
        elif len(sort_in_seq) == unique_count:
            if tmp_size < min_size:
                min_size = tmp_size
                min_left = left+1
                min_right = right
            tmp_size -= 1
            sort_in_seq[seq[left]] -= 1
            if sort_in_seq[seq[left]] == 0:
                del sort_in_seq[seq[left]]
            left += 1 # Update pointer.
    return (min_left, min_right)
    
def main():
    # Read data from file.
    finput = open("input.txt", "r")
    tree_count, sort_count = tuple(map(int, finput.readline().split()))
    tree_list = [0] * tree_count

    # Fill tree list.
    ctr = 0
    for tree in map(int, finput.readline().split()):
        tree_list[ctr] = tree
        ctr += 1
    
    finput.close()
        
    # Analyze data.
    ans = find_shortest_seq(tree_list, sort_count)

    # Write answer.
    foutput = open("output.txt", "w")
    foutput.write(f"{ans[0]} {ans[1]}")
    foutput.close()

main()