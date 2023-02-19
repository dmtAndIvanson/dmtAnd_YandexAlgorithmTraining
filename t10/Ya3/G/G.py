# Создать словарь - {(a,b): ctr}.
# Проверить есть ли данное значение в словаре.
def read_data(file, size):
    """Read pair values from file."""
    state = []
    for i in range(size):
        (a, b) = tuple(map(int, file.readline().split()))
        state.append((a, b))

    return state


def main():
    # Read data.
    file = open("input.txt", "r")

    turtles = int(file.readline())

    state = read_data(file, turtles)

    file.close()

    # Analyze data.
    dict1 = {}
    for i in range(turtles): # Fill dict1 with possible statements.
        dict1[(i,turtles-i-1)] = 0

    # Count how many true states.
    true_state = 0
    for i in state:
        if i in dict1 and dict1[i] == 0:
            dict1[i] = 1
            true_state += 1

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{true_state}")

    file.close()


main()