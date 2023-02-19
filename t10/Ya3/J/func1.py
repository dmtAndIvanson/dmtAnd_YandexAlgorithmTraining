# Создать словарь точек, где может быть объект.
# В создании уситывать максимальное расстояние от самой точки (если она первая)
# Или краевых точек, если их много

def create_points(n_point, old, size, limit):
    """Create dictionary, where points can be."""
    x, y = n_point

    new = {(x,y): True}

    for i in range(size+1):
        for j in range()\


             if i == 0:
                    if abs(sx-x) + abs(sy-y-j) <= limit and abs(sx-x) + abs(sy-y-j) <= d:
                        dict2[(x,y+j)] = True
                    if abs(sx-x) + abs(sy-y+j) <= limit and abs(sx-x) + abs(sy-y+j) <= d:
                        dict2[(x,y-j)] = True
                    if abs(sx-x-j) + abs(sy-y) <= limit and abs(sx-x-j) + abs(sy-y) <= d:
                        dict2[(x+j,y)] = True
                    if abs(sx-x+j) + abs(sy-y) <= limit and abs(sx-x+j) + abs(sy-y) <= d:
                        dict2[(x-j,y)] = True
                else:
                    if abs(sx-x-j) + abs(sy-y-j) <= limit and abs(sx-x-j) + abs(sy-y-j) <= d:
                        dict2[(x+j,y+j)] = True
                    if abs(sx-x-j) + abs(sy-y+j) <= limit and abs(sx-x-j) + abs(sy-y+j) <= d:
                        dict2[(x+j,y-j)] = True
                    if abs(sx-x+j) + abs(sy-y-j) <= limit and abs(sx-x+j) + abs(sy-y-j) <= d:
                        dict2[(x-j,y+j)] = True
                    if abs(sx-x+j) + abs(sy-y+j) <= limit and abs(sx-x+j) + abs(sy-y+j) <= d:
                        dict2[(x-j,y-j)] = True