def findclosestnuminlist(list1, list2):
    """
    For every element in the second list
    Check if number is in the first list.
    And write answer to the file.
    """
    file = open("output.txt", "w")
    for num in list2:
        closestnum = binsearch(0, len(list1)-1, list1, num)
        file.write(f"{closestnum}\n")
    file.close()
    
    
def binsearch(l, r, nums, value):
    while l < r:
        # Choose element in the middle.
        m = (l+r+1) // 2
        if nums[m] > value:
            if l < m and abs(nums[m] - value) < abs(nums[m-1] - value):
                l = m
            else:
                r = m - 1
        else:
            l = m
    return nums[l]
    
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
    findclosestnuminlist(list1, list2)

main()
