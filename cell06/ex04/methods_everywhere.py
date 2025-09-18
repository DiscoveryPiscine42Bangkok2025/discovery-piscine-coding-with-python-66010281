import sys
def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s + "Z" * (8 - len(s)))

args = sys.argv[1:]

if len(args) < 1:
    print("none")
else:
    for word in args:
        if len(word) < 8:
            enlarge(word)
        elif len(word) > 8:
            shrink(word)
        else:
            print(word)
