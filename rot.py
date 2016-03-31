#helper with alphabet to number conversion and mod math
#brupoon


def caesar(string, rot):
    
    string_lower = string.lower()
    string_rot = ""

    for i in range(0,len(string_lower)):
        old_ord = ord(string_lower[i])-97
        new_ord = (old_ord + rot) % 26 + 97

        new_ord = chr(new_ord)
        string_rot += new_ord

    return string_rot

def mod26(a):
    return a % 26

this = input("string?")
rot = input("rot?")
rot = int(rot)

print(caesar(this,rot))
