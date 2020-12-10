#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{}".format(len(sys.argv) - 1), end="")
    if (len(sys.argv) == 1):
        print(" arguments.")
    elif (len(sys.argv) == 2):
        print(" argument:")
        print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print(" arguments:")
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
