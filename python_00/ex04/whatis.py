import sys

if (len(sys.argv) == 1):
    sys.exit()

try:
    errMsg = "AssertionError: More than 1 argument provided."
    assert (len(sys.argv) == 2), errMsg
    num = int(sys.argv[1])
    if (num % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("ValueError : consists of not number")
except AssertionError as msg:
    print(msg)
