def find_substring_with_k_elements(string, n, k):
        # Substring has k same elments.
    # Find longest substring in string.
    left = 0
    right = 0

    letter_count = {}

    max_len = 0
    start = 0

    while right < n and left <= right:
        if string[right] not in letter_count:
            letter_count[string[right]] = 0
        letter_count[string[right]] += 1
        while letter_count[string[right]] > k:
            letter_count[string[left]] -= 1
            left += 1
        if right-left+1 > max_len:
            max_len = right-left+1
            start = left+1
        right += 1

    return (max_len, start)    

def main():
    # Read data from file.
    finput = open("input.txt", "r")

    n, k = list(map(int, finput.readline().split()))
    string = finput.readline().strip()

    finput.close()

    # Analyze data.
    max_len, start = find_substring_with_k_elements(string, n, k)

    # Write answer to file.
    foutput = open("output.txt", "w")

    foutput.write(f"{max_len} {start}")

    foutput.close()

main()