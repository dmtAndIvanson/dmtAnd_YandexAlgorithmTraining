def find_accent(word):
    """Find accent places in word."""
    accent_place = set()
    
    for i in range(len(word)):
        if word[i].isupper():
            accent_place.add(i)

    return accent_place


def read_dict(file):
    """Read dictionary from file."""
    word_dict = {}

    ctr = int(file.readline())
    for i in range(ctr):
        word = file.readline().strip()

        accent = find_accent(word)

        key = word.lower()
        if key not in word_dict:
            word_dict[key] = set()

        for i in accent:
            word_dict[key].add(i)

    return word_dict


def is_right_accent(word, word_dict):
    """Find whether word is in dictionary.
       Return 1 if accent is right, 0 otherwise."""
    key = word.lower()
    accent = find_accent(word)

    if key not in word_dict:
        return 1 if len(accent) == 1 else 0

    elif len(accent) != 1:
        return 0

    else:
        for i in accent:
            if i in word_dict[key]:
                return 1

    return 0


def main():
    # TODO:
    # Make word-dictionary {'lowercase word': set(accent place)}.
    # If word is not in dictionary and has one accent - it's writen right.
    # If word is in dictionary and compare accent place.
    # If word has many accents, compare with dictionary. If it's not in dictionary - count mistake.

    # Make function to find accent places. If no accent place, return -1 and count mistake.
    # For each word check whether it's in dictionary.

    # Read data.
    file = open("input.txt", "r")

    # Read dictionary.
    word_dict = read_dict(file)
    #print(word_dict)

    word_list = file.readline().split()

    ctr = 0
    for i in word_list:
        ans = is_right_accent(i, word_dict)
        ctr += 1 if ans == 0 else 0
        #print(i, ans)

    file.close()

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{ctr}")

    file.close()


main()