def count_similar(word, seq):
    """Find how often word is met in sequence."""
    ltr_dict = {}

    # Count how many times letter is met in word.
    for ltr in word:
        if ltr not in ltr_dict:
            ltr_dict[ltr] = 0
        ltr_dict[ltr] += 1
    
    # Make dictionary for words in letter with 0 count.
    empty_dict = {}

    for ltr in ltr_dict:
        empty_dict[ltr] = 0

    # Check every letter in word.
    w_ctr = 0
    len_str = 0
    start = 0
    ptr = 0

    tmp_dict = empty_dict.copy()
    while ptr < len(seq):
        # If letter is not in word, go ahead.
        if seq[ptr] not in ltr_dict:
            ptr += 1
            start = ptr
            tmp_dict = empty_dict.copy()
            len_str = 0
            continue

        # If letter is in word, count it.
        tmp_dict[seq[ptr]] += 1
        len_str += 1


        # If letter is met more, than should be, upadate data.
        if tmp_dict[seq[ptr]] > ltr_dict[seq[ptr]]:
            # Update where start is, and remove some data.
            while seq[start] != seq[ptr]:
                len_str -= 1
                tmp_dict[seq[start]] -= 1
                start += 1
            len_str -= 1
            tmp_dict[seq[start]] -= 1
            start += 1

        # When each letter in sequence matches with word, update data.
        if len_str == len(word):
            w_ctr += 1
            tmp_dict[seq[start]] -= 1
            start += 1
            len_str -= 1

        ptr += 1

    return w_ctr
            

def read_data(file):
    """Read data from file."""
    file.readline()
    word = file.readline()
    seq = file.readline()

    return (word[:-1], seq[:-1])


def main():
    # Read data.
    file = open("input.txt", "r")

    word, seq = read_data(file)

    file.close()

    # Find answer.
    ans = count_similar(word, seq)

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{ans}")

    file.close()


main()
