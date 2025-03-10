#!/usr/bin/env python3
import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def main():
    """
        Arg: Need a string as input
        Return: translated string to morse
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    string = sys.argv[1]
    translation = ""
    for c in string:
        morse = NESTED_MORSE.get(c.upper())
        if morse is None:
            raise KeyError("Char not translatable to morse")
        translation = translation + morse + " "
    translation = translation[:-1]
    print(translation)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(AssertionError.__name__ + f": {str(e)}")

    except KeyError as e:
        print(KeyError.__name__ + f"{str(e)}")
