#finding trigraphs in a given input file.
# requires input.txt to contain wanted input

input("please press enter if you have the input located in current wd as input.txt")
f = open('input.txt', 'r')

def get_letters(txt):
    return ''.join(filter(str.isalpha, txt))

text = f.read()
text = text.lower()
text = get_letters(text)
trigraphs = {} #dictionary of trigraphs hehehe

for letter in range(len(text)-3):
    tri = text[letter:letter+3]
    if tri in trigraphs:
        trigraphs[tri] += 1
    else:
        trigraphs[tri] = 1

trigraphs_sorted = sorted(trigraphs, key=trigraphs.get, reverse=True) #sort by frequency, high first

print("\n")
print(trigraphs)

print("trigraphs sorted \n")
print(trigraphs_sorted)
