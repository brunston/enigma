#attempting to find key collisions for multiplicative cipher
#of format x -> (x*n) mod k

k_length = input("k length?")
k_length = int(k_length)
n = input("n?")
n = int(n)

for i in range(26):
    print("(i*n) mod k: {0}".format((i*n)%k_length))
