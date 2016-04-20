# BRUTE FORCE find the inverse of a given number a in z
# brupoon

z = int(input("z (int)? "))
a = int(input("a (int)? "))
inverse = -1
for i in range(z):
    potential_inverse = (a*i) % z

    if (potential_inverse)==1:
        inverse = i
        print("gcd is 1. Inverse: {0}".format(i))
    else:
        print("Not inverse. a*i in Z: {0}".format(potential_inverse))

print("inverse (if -1 doesn't exist): {0}".format(inverse))
