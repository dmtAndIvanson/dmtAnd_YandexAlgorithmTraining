SIZE = 100 # Size of hashtable.


def main():
    x_vals = {} # Store possible x-axis values.

    # Read file.
    file = open("input.txt", "r")

    ctr = int(file.readline())
    for i in range(ctr):
        a, b = list(map(int, file.readline().split()))

        if a not in x_vals:
            x_vals[a] = True

    file.close()

    # Analyze data.
    ans = len(x_vals)

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{ans}")

    file.close()


main()