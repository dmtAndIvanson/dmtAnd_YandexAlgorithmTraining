def read_data(file):
    """Read sequence from file."""
    line = file.readline()

    size = int(line)

    line = file.readline()
    
    seq = list(map(int, line.split()))

    return (size, seq)


def find_person_score(size, seq):
    """Find person in sequence of results."""
    # Find top score in sequence.
    if size < 3:
        return 0

    top_score = seq[0]
    for i in range(1, size):
        if seq[i] > top_score:
            top_score = seq[i]

    # Find persons score in sequence.
    person_score = 0
    for i in range(1,size - 1):
        # Conditions that person present.
        if (seq[i] % 10) == 5 and seq[i-1] == top_score and\
            seq[i] > seq[i+1] and seq[i] > person_score: # Last condition to find highest possible place.
            person_score = seq[i]

    return person_score
    

def find_person_place(size, seq, score):
    """Find place of person."""
    if score == 0:
        return 0

    # Make sorted list of unique values.
    seq.sort(reverse=True)

    # Find persons place.
    place = 0
    for i in range(len(seq)):
        if seq[i] == score:
            place = i + 1
            break

    return place


def main():
    # Read data.
    file = open("input.txt", "r")

    size, seq = read_data(file)

    file.close()

    # Find persons score.
    score = find_person_score(size, seq)

    # Find persons place.
    ans = find_person_place(size, seq, score)

    # Write answer.
    file = open("output.txt", "w")

    file.write(str(ans))

    file.close()


main()