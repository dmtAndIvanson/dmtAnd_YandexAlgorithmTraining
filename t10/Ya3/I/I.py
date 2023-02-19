def read_data(file):
    """Read data from file."""
    lges = {}

    ctr1 = int(file.readline())
    for i in range(ctr1):
        ctr2 = int(file.readline())
        for j in range(ctr2):
            lang = file.readline().strip('\n')
            
            if lang not in lges:
                lges[lang] = 1
            else:
                lges[lang] += 1

    return (ctr1, lges)



def main():
    # Read data.
    file = open("input.txt", "r")

    total, lges = read_data(file)

    file.close()

    # Analyze data.
    list1 = [] # List of languages everybody know.
    for i in lges:
        if lges[i] == total:
            list1.append(i)

    # Write answer.
    file = open("output.txt", "w")

    if len(list1) > 0:
        file.write(f"{len(list1)}\n")

        for i in list1:
            file.write(i + "\n")

    else:
        file.write('0\n\n')

    file.write(f"{len(lges)}\n")

    for i in lges:
        file.write(i + "\n")

    file.close()


main()