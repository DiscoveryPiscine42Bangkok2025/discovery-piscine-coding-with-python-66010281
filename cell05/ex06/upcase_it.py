import sys
if len(sys.argv) > 1:
    all_args = ' '.join(sys.argv[1:])
    print(all_args.upper())
else:
    print("none")
