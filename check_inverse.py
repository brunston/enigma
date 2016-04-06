#check to see if an inverse in Z is valid:

x = int(input("x (int)? "))
x_inv = int(input("x inverse (int)? "))
z = int(input("z (int)? "))

if ((x*x_inv) % z) == 1:
    print("Inverse is valid")
else:
    print("Inverse is not valid")
