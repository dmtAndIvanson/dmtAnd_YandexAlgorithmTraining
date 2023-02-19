import math


def analyze_data(file1, file2):
    """Read and write data."""
    p_dict = {}

    line = file1.readline()
    while line != "":
        w_list = line.split()

        # View balance of a person.
        if w_list[0] == "BALANCE":
            if w_list[1] not in p_dict:
                file2.write("ERROR\n")
            else:
                file2.write(f"{p_dict[w_list[1]]}\n")

        # Give money to each person.
        elif w_list[0] == "INCOME":
            for i in p_dict:
                if p_dict[i] > 0:
                    percent = int(w_list[1]) / 100
                    p_dict[i] += math.floor(p_dict[i] * percent)

        # Transfer money from one person to another.
        elif w_list[0] == "TRANSFER":
            if w_list[1] not in p_dict:
                p_dict[w_list[1]] = 0

            if w_list[2] not in p_dict:
                p_dict[w_list[2]] = 0

            money = int(w_list[3])

            p_dict[w_list[1]] -= money
            p_dict[w_list[2]] += money

        # Add money to person.
        elif w_list[0] == "DEPOSIT":
            if w_list[1] not in p_dict:
                p_dict[w_list[1]] = 0

            money = int(w_list[2])
            p_dict[w_list[1]] += money

        # Take money from person.
        elif w_list[0] == "WITHDRAW":
            if w_list[1] not in p_dict:
                p_dict[w_list[1]] = 0

            money = int(w_list[2])
            p_dict[w_list[1]] -= money

        line = file1.readline()


def main():
    # Open file to read.
    input1 = open("input.txt", "r")
    output1 = open("output.txt", "w")

    # Analyze data.
    analyze_data(input1, output1)

    # Close files.
    input1.close()
    output1.close()


main()