import sys
if len(sys.argv) > 2:
    for argv in reversed(sys.argv[1:]):
        print(argv)
else:
    print("none")
