k_dict = {} # Dictionary for keywords.

w_dict = {} # Dictionary for all possible words.

w_list = [] # List for words.

# Write function, that separates sequence of numbers and characters from other text.
def separate_string_1(string):
    """Separate string, when register is crucial."""
    i = 0
    while i < len(string):
        w_tmp = []
        while string[i].isalnum() or string[i] == '_':
            w_tmp.append(string[i])
            i += 1
        if len(w_tmp) != 0:
            word = ''.join(map(str,w_tmp))
            if word not in k_dict and word.isnumeric() == False:
                if word not in w_dict:
                    w_dict[word] = 0
                    w_list.append(word)
                w_dict[word] += 1
        i += 1

    return w_dict


def separate_string_2(string):
    """Separate string, when register is not crucial."""
    i = 0
    while i < len(string):
        w_tmp = []
        while string[i].isalnum() or string[i] == '_':
            w_tmp.append(string[i].lower())
            i += 1
        if len(w_tmp) != 0:
            word = ''.join(map(str,w_tmp))
            if word not in k_dict and word.isnumeric() == False:
                if word not in w_dict:
                    w_dict[word] = 0
                    w_list.append(word)
                w_dict[word] += 1
        i += 1

    return w_dict


def fill_identifiers(file):
    """Read file. Fill dictionary with identifiers and return to flags."""
    ctr, flag1, flag2 = file.readline().split()
    ctr = int(ctr)

    for i in range(ctr):
        word = file.readline().strip()
        if flag1 == "yes":
            k_dict[word] = True
        else:
            word = word.lower()
            k_dict[word] = True

    return flag1, flag2


def read_program(file, register):
    """Read text of program in file."""
    line = file.readline()
    while line != "":
        if register == "yes":
            separate_string_1(line)
        else:
            separate_string_2(line)
        line = file.readline()


def main():
    # Read data.
    with open("input.txt", "r") as file:
        register, first_num = fill_identifiers(file)

        read_program(file, register)

    # If first_num flag is 'no'. Remove words beginning with nember.
    if first_num == 'no':
        keys = list(w_dict.keys())
        for i in keys:
            if i[0].isnumeric():
                w_dict.pop(i)

    # Find most often met word.
    max = 0
    for i in w_dict:
        if w_dict[i] > max:
            max = w_dict[i]

    max_set = set()
    for i in w_dict:
        if w_dict[i] == max:
            max_set.add(i)

    ans = ''
    for i in w_list:
        if i in max_set:
           ans = i
           break

    # Write answer.
    with open("output.txt", "w") as file:
        file.write(f"{ans}")


main()