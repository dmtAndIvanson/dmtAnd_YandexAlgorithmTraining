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
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def findsize(params):
    w, h, n = params
    count1 = rbinsearch(1, 2*n, checkenoughspace, params)
    count1 *= w
    count2 = rbinsearch(1, 2*n, checkenoughspace, (h,w,n))
    count2 *= h
    return count1 if count1 < count2 else count2

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
    # Write answer.
    #print(size)
    writeanswer(size)

main()