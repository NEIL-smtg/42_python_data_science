import sys

if (len(sys.argv) == 1):
    sys.exit()

try:
    errMsg = "AssertionError: More than 1 argument provided."
    assert (len(sys.argv) == 2), errMsg
    num = int(sys.argv[1])
    msg = "I'm Even" if (num % 2 == 0) else "I'm odd"
    print(msg)
except ValueError:
    print("ValueError : consists of not number")
except AssertionError as msg:
    print(msg)
