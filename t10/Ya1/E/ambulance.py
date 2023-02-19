# Программа-решение домашней задачи по алгоритмам.
# Формат ввода:
# 89 20 41 1 11

import math


def read_file(file):
    """Reads strings. Transforms strings to variabiles."""
    str1 = file.readline()
    flat1, max_floor, flat2, entrance2, floor2 = list(map(int, str1.split()))

    return flat1, max_floor, flat2, entrance2, floor2


def find_flats(entrance2, floor2, flat2, max_floor):
    """Find flats on floor"""
    # Check correctness of input data.
    if floor2 > max_floor:
        return -1
    
    # How many floors up to current flat.
    floors = (entrance2 - 1) * max_floor + floor2

    # How many flats on floor.
    flat_on_floor = math.ceil(flat2 / floors)

    # print(floors, flat_on_floor)
    return flat_on_floor



def find_entrance_floor(flat1, flats_on_floor, max_floors):
    """Find entrance and floor for flat."""
    # Find entrance.
    entrance = math.ceil(flat1 / (flats_on_floor * max_floors))

    # Find floor.
    floor = math.ceil((flat1 - (entrance - 1) * max_floors * flats_on_floor) / flats_on_floor)

    # print(entrance, floor)

    return entrance, floor


def write_answer(file, answer):
    """Write answer to file."""
    file.write(str(answer))


def main():
    # Read data from file
    file = open("input.txt", "r")

    flat1, max_floor, flat2, entrance2, floor2 = read_file(file)

    file.close()

    # Find how many flats on one floor.
    flats_on_floor = find_flats(entrance2, floor2, flat2, max_floor)

    if flats_on_floor == -1:
        # Write answer to file.
        file = open("output.txt", "w")

        answer = f"{-1} {-1}"

        write_answer(file, answer)

        file.close()

        exit()

    # Find entrance and floor.
    entrance1, floor1 = find_entrance_floor(flat1, flats_on_floor, max_floor)

    # Write answer to file.
    file = open("output.txt", "w")

    answer = f"{entrance1} {floor1}"

    write_answer(file, answer)

    file.close()


main()