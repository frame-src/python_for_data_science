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
            raise AssertionError()
        iterable = sys.argv[1].split(" ")
        try:
            min_len = int(sys.argv[2])
            print(list(ft_filter(lambda a: len(a) > min_len, iterable)))

        except ValueError:
            print("ValueError: Pleas give integer as second parameter")

    except AssertionError:
        print("AssertionError: AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
