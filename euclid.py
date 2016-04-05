# euclid's algorithm for GCD

import math

user_z = int(input("Choose a Z int: "))
user_x = int(input("Choose an X int: "))

def gcd(x,z):
    shift = True
    stor = 0
    while shift == True:
        stor = z
        z = x % z
        x = stor
        if z == 0:
            #print("second-to-last, {0}".format(stor))
            shift = False
    return x

print("\ngcd of {0},{1}: {2}\n\n".format(user_x,user_z,gcd(user_x,user_z)))

print("relative prime pairs in Z_{0}".format(user_z))
for i in range(1,user_z):
    if gcd(i,user_z) == 1:
        print("x: {0}, z: {1}".format(i, user_z))
