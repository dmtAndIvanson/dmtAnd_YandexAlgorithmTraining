# Make matrix with bombs '*'.
# For every not-bomb element count surrounding bombs.
# Transform this matrix to .txt file.


def insert_bombs(field, bomb_pos):
    """Fill field with bombs."""
    for pos in bomb_pos:
        field[pos[0]-1][pos[1]-1] = '*' # Minus one because of representation of coordinate.

    return field


def fill_field(field, rows, cols):
    """Fill field with numbers, which correspond to amount of neighbouring bombs."""
    for i in range(rows):
        for j in range(cols):
            if field[i][j] != '*':
                # Check surrounding symbols.
                # Add one to field[i][j] if symbol is '*'.
                b_ctr = 0

                for k in [-1,0,1]:
                    if (k + i < 0) or (k + i >= rows):
                        continue

                    for l in [-1,0,1]:
                        if (l + j < 0) or (l + j >= cols):
                            continue
                        
                        if field[k+i][l+j] == '*':
                            b_ctr += 1

                field[i][j] = b_ctr

    return field


def write_field(file, field):
    """Write field to file."""
    for i in field:
        line = ' '.join(map(str, i))
        file.write(line + '\n')


def main():
    # Read data from input-file.
    file = open("input.txt", "r")

    rows, cols, bomb_count = list(map(int, file.readline().split()))

    bomb_pos = []

    for i in range(bomb_count):
        coord = tuple(map(int, file.readline().split()))

        bomb_pos.append(coord)

    file.close()

    # Make field with zeroes. Each zero represents position in field.
    field = [[0 for i in range(cols)] for i in range(rows)]

    # Insert bombs according to their coordinates.
    field = insert_bombs(field, bomb_pos)

    # Update numbers in field.
    # So that number is amount of neighbouring '*'.
    field = fill_field(field, rows, cols)    
                    
    # Write field to file.
    file = open("output.txt", "w")

    write_field(file, field)

    file.close()


main()