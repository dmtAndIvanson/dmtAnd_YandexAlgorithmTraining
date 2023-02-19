# Поезд стоит на платформе 1 минуту
# Поезд приезжает через a-минут на первую платформу
#                       b-минут на вторую платформу

# Формат ввода:
# a - интервал на первом пути
# b - интервал на втором пути
# n - поездов на первом пути
# m - поездов на втором пути

# Найти:
# минимальное и максимальное время, которое Таня могла стоять на платформе

def find_shortest(int1, int2, tr1, tr2):
    """Find the shortest time for waiting."""
    # Guess int1 > int2
    s_time = int2 * tr2 + tr2 - 1

    return s_time


def find_longest(int1, int2, tr1, tr2):
    """Find the longest time for waiting."""
