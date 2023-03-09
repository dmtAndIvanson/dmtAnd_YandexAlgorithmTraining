from math import ceil

def writeanswer(answer):
    file = open("output.txt", "w")
    file.write(f"{answer}")
    file.close()
        
def checkenoughspace(val, checkparams):
    w, h, n = checkparams
    side1 = val * w
    side2 = h * ceil(n / val)
    return side1 >= side2

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if checkenoughspace(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def findsize(params):
    w, h, n = params
    count = rbinsearch(1, n, checkenoughspace, params)
    return count * (w if w > h else h)

def read_data():
    file = open("input.txt", "r")
    w, h, n = map(int, file.readline().split())
    file.close()
    return w, h, n

def main():
    # Read data.
    w, h, n = read_data()
    # Analyze data.
    size = findsize((w, h, n))
    print(size)
    # Write answer.
    writeanswer(size)

main()