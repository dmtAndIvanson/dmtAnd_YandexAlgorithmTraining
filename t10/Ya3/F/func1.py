def analyze_2(line1, line2):
    table = [[0 for i in range(26)] for i in range(26)]

    # Count every pair. 
    for ctr in range(len(line1) - 1):
        i = ord(line1[ctr]) - 65
        j = ord(line1[ctr+1]) - 65

        table[i][j] += 1

    # Count common pairs.
    common = 0

    for ctr in range(len(line2) - 1):
        i = ord(line2[ctr]) - 65
        j = ord(line2[ctr+1] - 65

        if table[i][j] != 0:
            common += table[i][j]
            table[i][j] = 0
            
    return common
    

def main():
    # Read data.
    file = open("input.txt", "r")

    line = file.readline().rstrip('\n')
    line2 = file.readline().rstrip('\n')

    file.close()

    # Analyze data.
    common = analyze(line, line2)

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{common}")

    file.close()


main()