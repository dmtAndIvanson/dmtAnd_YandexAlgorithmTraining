def read_data(file):
    """Read data from file. *It should be sequence of numbers.
       Sequence terminates with -2000000000."""
    seq = []
    line = file.readline()

    while(line != '-2000000000' and line != ''):
        seq.append(int(line))

        line = file.readline()

    return seq


def determine_type(seq):
    """Determine type of sequence.
       Types: CONSTANT, ASCENDING, WEAKLY ASCENDING,
              RANDOM,  DESCENDING, WEAKLY DESCENDING"""
    if len(seq) < 1:
        return "RANDOM"
    elif len(seq) == 1:
        return "CONSTANT"

    # Possible relations between neighbor numbers in sequence.
    case1 = {"equal" : 0, "more" : 0, "less" : 0}

    # Count each passible case.
    for i in range(len(seq) - 1):
        if seq[i] == seq[i+1]:
            case1["equal"] += 1

        elif seq[i] < seq[i+1]:
            case1["more"] += 1

        elif seq[i] > seq[i+1]:
            case1["less"] += 1

    # Determine type of sequence.
    if case1["equal"] == (len(seq) - 1):
        return "CONSTANT"
    
    elif case1["more"] == (len(seq) - 1):
        return "ASCENDING"

    elif case1["less"] == (len(seq) - 1):
        return "DESCENDING"

    elif (case1["equal"] + case1["more"]) == (len(seq) - 1):
        return "WEAKLY ASCENDING"

    elif (case1["equal"] + case1["less"]) == (len(seq) - 1):
        return "WEAKLY DESCENDING"
    
    else:
        return "RANDOM"


def write_answer(file, ans):
    """Write answer to file."""
    file.write(ans)


def main():
    # Read data from file.
    file = open("input.txt", "r")

    seq = read_data(file)

    file.close()

    # Determine type of sequence.
    ans = determine_type(seq)

    # Write answer.
    file = open("output.txt", "w")

    write_answer(file, ans)

    file.close()


main()