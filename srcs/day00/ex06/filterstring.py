#!/usr/bin/env python3
import sys
from ft_filter import ft_filter


def main():
    """
        Args:
            - one a String that goes as iterable
            - integer for min-len
        Return Value:
            - return a list that contains all the words which len
              is bigger than the given integer
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        iterable = sys.argv[1].split(" ")
        try:
            min_len = int(sys.argv[2])
            print(list(ft_filter(lambda a: len(a) > min_len, iterable)))

        except ValueError:
            print(ValueError.__name__ + ": Please give integer as second parameter")

    except AssertionError as e:
        print(AssertionError.__name__ + f": {str(e)}")


if __name__ == "__main__":
    main()
