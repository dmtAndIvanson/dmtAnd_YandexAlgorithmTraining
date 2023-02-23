# Version with two pointers.

def find_greater_distance_count(seq, distance):
    """Find how many objects with distance greater than distance in argument."""
    seq_length = len(seq)
    left = right = 0 # Set pointers.
    ctr = 0
    
    if distance == 0:
        ctr = seq_length * (seq_length-1) // 2 + seq_length
    else:
        while right < seq_length and left <= right: # Check if distance equals 0.
            if seq[right] - seq[left] > distance:
                ctr += seq_length - right
                left += 1
            else:
                right += 1

    return ctr

def main():
    # Read data from file.
    finput = open("input.txt", "r")
    monuments, min_distance = tuple(map(int, finput.readline().split()))
    monuments_location = list(map(int, finput.readline().split()))
    finput.close()

    # Analyze data.
    good_locations = find_greater_distance_count(monuments_location, min_distance)

    # Write answer.
    foutput = open("output.txt", "w")
    foutput.write(f"{good_locations}")
    foutput.close()

main()