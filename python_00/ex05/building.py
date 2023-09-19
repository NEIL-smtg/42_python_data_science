import sys


def main():
    '''
        if current file is being run directly ,
        __name__ will be "__main__"
        else if this file is being imported, the __name__
        of this file will be its filename
    '''
    try:
        ac = len(sys.argv)
        assert ac <= 2, "AssertionError: Invalid number of arguments."

        if (ac == 1 or sys.argv[1] is None):
            print("What is the test to count ?")
            inp = sys.stdin.readline()
        else:
            inp = sys.argv[1]

        up = low = dig = punc = sp = 0

        for c in inp:
            if (c.islower()):
                low += 1
            elif (c.isupper()):
                up += 1
            elif (c.isdigit()):
                dig += 1
            elif (c.isspace()):
                sp += 1
            elif (c.isprintable()):
                punc += 1
        print("The text contains", len(inp), "characters: ")
        print(up, " upper letters")
        print(low, " lowercase letters")
        print(punc, " punctuation letters")
        print(sp, " spaces")
        print(dig, " digits")
    except KeyboardInterrupt:
        print("\nCtrl+c pressed..Exiting...")
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
