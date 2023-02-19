def find_two_lowest_pos_neg(seq):
    """Return two lowest negative and two lowest positive numbers"""
    # Find two highest positive and two lowest negative numbers.
    l_pos1 = float('inf')
    l_pos2 = float('inf')

    l_neg1 = float('-inf')
    l_neg2 = float('-inf')

    for i in seq: # There is easier way to find numbers.
        if i >= 0:
            if l_pos1 == float('inf'):
                l_pos1 = i

            elif l_pos2 == float('inf'):
                l_pos2 = i if i <= l_pos1 else l_pos1
                l_pos1 = l_pos1 if i <= l_pos1 else i

            else:
                if i <= l_pos2:
                    l_pos1, l_pos2 = l_pos2, i

                elif i < l_pos1 and i != l_pos2:
                    l_pos1 = i

        else:
            if l_neg1 == float('-inf'):
                l_neg1 = i

            elif l_neg2 == float('-inf'):
                l_neg2 = i if i >= l_neg1 else l_neg1
                l_neg1 = l_neg1 if i > l_neg1 else i

            else:
                if i <= l_neg1:
                    l_neg1, l_neg2 = i, l_neg1

                elif i < l_neg2 and i != l_neg1:
                    l_neg2 = i

    return ([l_pos2, l_pos1], [l_neg2, l_neg1])


def find_three_highest_pos_neg(seq):
    """Return three highest negative and three lowest positive numbers"""
    m_neg1 = float("-inf")
    m_neg2 = float("-inf")
    m_neg3 = float("-inf")

    m_pos1 = float("-inf")
    m_pos2 = float("-inf")
    m_pos3 = float("-inf")

    for i in seq:
        if i >= 0: # For positive numbers.
            if i >= m_pos1:
                m_pos1, m_pos2, m_pos3 = i, m_pos1, m_pos2

            elif i >= m_pos2:
                m_pos2, m_pos3 = i, m_pos2

            elif i > m_pos3:
                m_pos3 = i

        else: # For negative numbers.
            if i >= m_neg1:
                m_neg1, m_neg2, m_neg3 = i, m_neg1, m_neg2

            elif i >= m_neg2:
                m_neg2, m_neg3 = i, m_neg2

            elif i > m_neg3:
                m_neg3 = i

    return ([m_pos1, m_pos2, m_pos3], [m_neg1, m_neg2, m_neg3])


def find_max_product(l_pos, l_neg, m_pos, m_neg):
    """Find three numbers with the highest product."""
    if len(m_pos) == 3:
        if len(l_neg) != 2:
            return m_pos

        elif len(l_neg) == 2:
            return m_pos if seq_prod(l_neg)*m_pos[0] < seq_prod(m_pos) else [m_pos[0], l_neg[0], l_neg[1]]

    else:
        if len(l_pos) == 2:
            return [l_pos[0], l_neg[0], l_neg[1]] if len(l_neg) == 2 else [l_pos[0], l_pos[1], m_neg[0]]
            
        elif len(l_pos) == 1:
            return [l_pos[0], l_neg[0], l_neg[1]]

        else:
            return m_neg


def seq_prod(seq):
    """Find product od numbers in sequence."""
    product = 1

    for i in seq:
        product *= i

    return product


def remove_infinity(seq):
    """Remove '-inf' from seq."""
    seq = [i for i in seq if i != float('-inf') and i != float('inf')]
    seq.sort(reverse=True)
    return seq



def main():
    # Read data.
    file = open("input.txt", "r")

    seq = list(map(int, file.readline().split()))

    file.close()

    # Find set of numbers.
    a, b = find_two_lowest_pos_neg(seq)

    c, d = find_three_highest_pos_neg(seq)

    # Remove infinities.
    a = remove_infinity(a)
    b = remove_infinity(b)
    c = remove_infinity(c)
    d = remove_infinity(d)

    #print(a,b,c,d)

    # Find which numbers give the highest products.
    ans = find_max_product(a, b, c, d)

    line = ' '.join(map(str, ans))

    # Write answer.
    file = open("output.txt", "w")

    file.write(line)

    file.close()


main()