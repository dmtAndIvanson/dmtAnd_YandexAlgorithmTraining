def find_edges(seq):
    """Return two lowest negative and two highest possible numbers"""
    # Find two highest positive and two lowest negative numbers.
    m_pos1 = float('inf')
    m_pos2 = float('inf')

    l_neg1 = float('-inf')
    l_neg2 = float('-inf')

    for i in seq:
        if i >= 0:
            if m_pos1 == float('inf'):
                m_pos1 = i

            elif m_pos2 == float('inf'):
                m_pos2 = i if i <= m_pos1 else m_pos1
                m_pos1 = m_pos1 if i < m_pos1 else i

            else:
                if i >= m_pos1:
                    m_pos1, m_pos2 = i, m_pos1

                elif i > m_pos2 and i != m_pos1:
                    m_pos2 = i

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

    ans = []
    for i in (m_pos1, m_pos2, l_neg1, l_neg2):
        if i != float('inf') and i != float('-inf'):
            ans.append(i)

    return ans


def max_product(seq):
    """Find numbers which product is the highest."""
    num1 = 0
    num2 = 0
    product = float("-inf")

    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[i] * seq[i+j+1] > product:
                num1, num2 = seq[i], seq[i+j+1]
                product = num1*num2
                #print(num1, num2, num1*num2)

    return (num1, num2) if num1 < num2 else (num2, num1)


def main():
    # Read data.
    file = open("input.txt", "r")

    seq = list(map(int, file.readline().split()))

    file.close()

    # Find the lowest and the highest numbers.
    edges = find_edges(seq)
    #print(edges)

    # Find numbers with the highest product.
    numbers = max_product(edges)
    #print(numbers)

    # Write answer.
    file = open("output.txt", "w")

    file.write(f"{numbers[0]} {numbers[1]}")

    file.close()


main()