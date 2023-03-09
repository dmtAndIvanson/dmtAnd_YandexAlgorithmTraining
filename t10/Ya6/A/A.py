def checklistinlist(list1, list2):
    """
    For every element in the second list
    Check if number is in the first list.
    And write answer to the file.
    """
    file = open("output.txt", "w")
    good = "YES\n"
    bad = "NO\n"
    for num in list2:
        if binsearch(0, len(list1)-1, list1, num):
            file.write(good)
        else:
            file.write(bad)
    file.close()
    
    
def binsearch(l, r, nums, value):
    while l < r:
        m = (l + r) // 2
        if nums[m] < value:
            l = m + 1
        else:
            r = m
    return value == nums[r]
    
def read_data():
    file = open("input.txt", "r")
    N, K = map(int, file.readline().split())
    list1 = list(map(int, file.readline().split()))
    list2 = list(map(int, file.readline().split()))
    file.close()
    return list1, list2

def main():
    # Read data from file.
    list1, list2 = read_data()
    # Sort values of the first list.
    list1.sort()
    # Analyze data.
    checklistinlist(list1, list2)

main()
