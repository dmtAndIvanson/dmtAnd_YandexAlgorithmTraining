def read_data(file):
    """Read sequence from file."""
    line = file.readline()

    size = int(line)

    line = file.readline()
    
    seq = list(map(int, line.split()))

    return (size, seq)


def mirror_seq(seq):
    # When symmetric sequence added.
    if is_mirror(seq) == True:
        return []

    mid = len(seq) // 2 # Element in the middle of the sequence.

    index1 = mid # Index for not-repeating element.

    # Even case.
    for i in range(index1):
        #print(seq[i*2:mid+i], seq[:mid-1+i:-1])
        if seq[i*2:mid+i] == seq[:mid-1+i:-1]: # Compare left and right sequences.
            index1 -= len(seq[i*2:mid+i])
            break
        index1 += 1

    add1 = seq[index1-1::-1]

    index2 = mid

    # Odd case.
    for i in range(index2-1):
        #print(seq[i*2+1:mid+i], seq[:mid+i:-1])
        if seq[i*2+1:mid+i] == seq[:mid+i:-1]: # Compare left and right sequences.
            index2 -= len(seq[i*2+1:mid+i])
            break
        index2 += 1

    add2 = seq[index2-1::-1]

    return add1 if add1 < add2 else add2


def is_mirror(seq):
    """Determine if sequence is symmetric."""
    mid = len(seq) // 2

    if (len(seq) % 2) == 1:
        return True if seq[:mid] == seq[:mid:-1] else False
    
    else:
        return True if seq[:mid] == seq[:mid-1:-1] else False


def write_data(file, seq):
    """Write data to file."""
    if len(seq) == 0:
        file.write('0')

    else:
        file.write(str(len(seq)) + '\n')

        line = ' '.join(map(str, seq))

        file.write(line)



def main():
    # Read data.
    file = open("input.txt", "r")

    size, seq = read_data(file)

    file.close()

    # Check if sequence is symmetric.
    if is_mirror(seq) == True:
        ans = []

    else:
        if (len(seq) % 2) == 0:
            ans = mirror_seq(seq)

        else:
            ans = mirror_seq(seq[1:]) + [seq[0],]


    # Write answer.
    file = open("output.txt", "w")

    write_data(file, ans)

    file.close()


main()