# Version with two pointers.
# In this version I declare list of values and then fill it.

def main():
    # Read data from file.
    finput = open("input.txt", "r")
    monuments, distance = tuple(map(int, finput.readline().split()))
    seq = [0] * monuments
    ctr = 0
    for i in map(int, finput.readline().split()):
        seq[ctr] = i
        ctr += 1

    # Fill seq.
    finput.close()

    # Analyze data.
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

    # Write answer.
    foutput = open("output.txt", "w")
    foutput.write(f"{ctr}")
    foutput.close()

main()