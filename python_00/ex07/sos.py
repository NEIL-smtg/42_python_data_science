import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def main():
    ac = len(sys.argv)
    errMsg = "Error: bad arguments"
    try:
        assert ac == 2, errMsg
        inp = sys.argv[1]
        res = ""

        for ch in inp:
            assert ch.isprintable() and (ch.isalnum() or ch.isspace()), errMsg
            if (ch.islower()):
                c = ch.upper()
            else:
                c = ch
            res += NESTED_MORSE.get(c)
        print(res)
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
