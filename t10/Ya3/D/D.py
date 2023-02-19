SIZE = 1000


def sum_letters(word):
    """Sum code of all letters in word."""
    word = word.lower()

    sum = 0
    for i in word:
        sum += ord(i)

    return sum


def main():
    # Make hashtable for storing words.
    table = [[] for i in range(SIZE)]

    # Read data.
    file = open("input.txt", "r")

    # Read line by line, while not EOF.
    while True:
        line = file.readline()

        if line == "":
            break

        seq = line.split()

        # For each word in line make hash-code.
        for word in seq:
            code = sum_letters(word) % SIZE

            # Check whether a word exists in hash table, append if not.
            if word not in table[code]:
                table[code].append(word)

    file.close()

    # Count how many words in table.
    w_count = 0
    for i in table:
        w_count += len(i)

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{w_count}")

    file.close()


main()