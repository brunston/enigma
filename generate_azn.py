# generate a*z_n = {ax : x in z_n} for any a in z_n
# brupoon

n = int(input("Z_n (integer n)? "))
a = int(input("a for a*Z_n (integer a)?"))
z_n = []
az_n = []
for i in range(n):
    # standard set z_n
    z_n.append(i)

for x in range(n):
    value = (a*x) % n
    # find ax in z_n
    az_n.append(value)

#az_n = sorted(az_n)

print("Z_n: {0}".format(z_n))
print("a*Z_n: {0}".format(az_n))
