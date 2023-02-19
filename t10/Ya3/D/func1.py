def main():
    file = open("input.txt", "r")

    while True:
        line = file.readline()

        if line == "":
            break

        print(line)
        
    file.close()


main()