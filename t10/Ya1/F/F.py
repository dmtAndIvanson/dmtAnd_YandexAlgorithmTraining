def read_data(file):
    """Read data from file."""
    line = file.readline()

    a1, b1, a2, b2 = list(map(int, line.split()))

    return a1, b1, a2, b2


def order_sides(a1, b1, a2, b2):
    """Side a should be bigger than side b."""
    if a1 < b1:
        a1, b1 = b1, a1
    
    if a2 < b2:
        a2, b2 = b2, a2

    # a-side of the first rectangle shold be bigger.
    if a1 < a2:
        a1, b1, a2, b2 = a2, b2, a1, b1

    return a1, b1, a2, b2


def find_table_side(a1, b1, a2, b2):
    """Find sizes of rectangle with the smallest square.
       That rectangle can handle two squares with sides a1, b1, a2, b2."""
    if a2 > b1:
        side1 = a1
        side2 = b1 + b2
    else:
        side1 = a1 + b2
        side2 = b1

    return side1, side2


def write_answer(file, a, b):
    """Write values of a and b to file."""
    line = f"{a} {b}"
    file.write(line)
    

def main():
    # Read data from file.
    file = open("input.txt", "r")
    
    a1, b1, a2, b2 = read_data(file)

    file.close()

    # Place the biggest side of table to a.
    a1, b1, a2, b2 = order_sides(a1, b1, a2, b2)

    # Find sizes of table sides.
    side1, side2 = find_table_side(a1, b1, a2, b2)

    # Write answer to file.
    file = open("output.txt", "w")

    write_answer(file, side1, side2)

    file.close()


main()