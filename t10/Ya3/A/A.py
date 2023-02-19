def main():
    # Read data from file.
    file = open("input.txt", "r")

    seq = set(map(int, file.readline().split()))

    file.close()

    # Analyze data.
    ans = len(seq)

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{ans}")

    file.close()


main()