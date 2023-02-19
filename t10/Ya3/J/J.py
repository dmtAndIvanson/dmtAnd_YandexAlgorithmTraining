# Создать словарь возможных координат точки 1.
# Создать словарь возможных координат точки 2.
# Для каждой точки из списка два
# Проверить, что можно добраться из каждой точки из списка 1.
# Можно ? тогда значение True : False.
# Найти все точки со значениями True.

def create_points_1(start, coord, d, limit):
    """Create list of coordinates with maximum sizes d."""
    sx, sy = start
    x, y = coord
    dict1 = {(x,y): True}

    # Create coordinates, that are in figure.
    for i in range(d+1):
        for j in range(1, d-i+1):
            if i == 0:
                if abs(sx-x) + abs(sy-y-j) <= limit:
                    dict1[(x,y+j)] = True
                if abs(sx-x) + abs(sy-y+j) <= limit:
                    dict1[(x,y-j)] = True
                if abs(sx-x-j) + abs(sy-y) <= limit:
                    dict1[(x+j,y)] = True
                if abs(sx-x+j) + abs(sy-y) <= limit:
                    dict1[(x-j,y)] = True
            else:
                if abs(sx-x-j) + abs(sy-y-j) <= limit:
                    dict1[(x+j,y+j)] = True
                if abs(sx-x-j) + abs(sy-y+j) <= limit:
                    dict1[(x+j,y-j)] = True
                if abs(sx-x+j) + abs(sy-y-j) <= limit:
                    dict1[(x-j,y+j)] = True
                if abs(sx-x+j) + abs(sy-y+j) <= limit:
                    dict1[(x-j,y-j)] = True

    return dict1


def create_points_2(dict1, coord, d, limit):
    """Create list of coordinates with maximum sizes d."""
    x, y = coord
    dict2 = {}

    for i in dict1:
        sx, sy = i
        if abs(sx-x) + abs(sy-y) <= limit:
            dict1[(x,y)] = True
            break

    for k in dict1:
        sx, sy = k
        # Create coordinates, that are in figure.
        for i in range(d+1):
            for j in range(1, d-i+1):
                if i == 0:
                    if abs(sx-x) + abs(sy-y-j) <= limit:
                        dict2[(x,y+j)] = True
                    if abs(sx-x) + abs(sy-y+j) <= limit:
                        dict2[(x,y-j)] = True
                    if abs(sx-x-j) + abs(sy-y) <= limit:
                        dict2[(x+j,y)] = True
                    if abs(sx-x+j) + abs(sy-y) <= limit:
                        dict2[(x-j,y)] = True
                else:
                    if abs(sx-x-j) + abs(sy-y-j) <= limit:
                        dict2[(x+j,y+j)] = True
                    if abs(sx-x-j) + abs(sy-y+j) <= limit:
                        dict2[(x+j,y-j)] = True
                    if abs(sx-x+j) + abs(sy-y-j) <= limit:
                        dict2[(x-j,y+j)] = True
                    if abs(sx-x+j) + abs(sy-y+j) <= limit:
                        dict2[(x-j,y-j)] = True

    return dict2

        


def main():
    # Read data.
    file = open("input.txt", "r")
    
    t, d, n = list(map(int, file.readline().split()))

    coord = tuple(map(int, file.readline().split()))

    dict1 = create_points_1((0,0), coord, d, t)
    
    # Analyze data.
    for i in range(n-1):
        coord = tuple(map(int, file.readline().split()))
        dict1 = create_points_2(dict1, coord, d, t)

    file.close()
    
    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{len(dict1)}\n")

    for i in dict1:
        file.write(f"{i[0]} {i[1]}\n")

    file.close()


    

main()