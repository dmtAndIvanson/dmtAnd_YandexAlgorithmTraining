comp = 19/23

for b in range(1,100):
    for d in range(1,100):
        for a in range(1,b):
            for c in range(1,d):
                if (a/b + c/d) == comp and a/b != c/d and (a%b) != 0 and (c%d) != 0:
                    print(f"{a/b}+{c/d}={comp}")
                    print(a,b,c,d)
                    exit()

"""
    for b in range(2,100):
        for d in range(b+1,100):
            if two_prime(b,d) == False:
                continue
            
            for a in range(1,b):
                for c in range(1,d):
                    if two_prime(a,c) == False:
                        continue

                    elif (a*d*q + b*c*q == 2*a*b*p):
                        return (a,b,c,d)
"""