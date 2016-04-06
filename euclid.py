# euclid's algorithm for GCD

import math

user_z = int(input("Choose a Z int: "))
user_x = int(input("Choose an X int: "))

def gcd(x,y):
    stor = 0
    while y !=0:
        stor = y # store old value of y
        y = x % y # new y value is now the remainder of x and y
        x = stor # x becomes old value of y
    
    #print("second-to-last, {0}".format(stor))
    return x

print("\ngcd of {0},{1}: {2}\n\n".format(user_x,user_z,gcd(user_x,user_z)))

print("relative prime pairs in Z_{0}".format(user_z))
for i in range(1,user_z):
    if gcd(i,user_z) == 1:
        print("x: {0}, z: {1}".format(i, user_z))
