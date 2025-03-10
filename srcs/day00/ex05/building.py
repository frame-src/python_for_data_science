#!/usr/bin/env python3
import sys
import string
from collections import Counter


class TextAnalyzer:
    def __init__(self, input_string):
        self.upper_case = set(string.ascii_uppercase)
        self.lower_case = set(string.ascii_lowercase)
        self.punctuation = set(string.punctuation)
        self.digits = set(string.digits)
        self.spaces = {' '}
        self.category_count = Counter({'upper_case': 0,
                                       'lower_case': 0,
                                       'punctuation': 0,
                                       'digits': 0,
                                       'spaces': 0
                                       })

        self.input_string = input_string
        self.analyze()

    def analyze(self):
        """Iterates over the string and classifies characters
            into categories."""
        for char in self.input_string:
            if char in self.upper_case:
                self.category_count['upper_case'] += 1
            elif char in self.lower_case:
                self.category_count['lower_case'] += 1
            elif char in self.punctuation:
                self.category_count['punctuation'] += 1
            elif char in self.digits:
                self.category_count['digits'] += 1
            elif char in self.spaces:
                self.category_count['spaces'] += 1

    def report(self):
        """Prints the results."""
        total_chars = len(self.input_string)
        print(f"The text contains {total_chars} characters:")
        print(f"{self.category_count['upper_case']} upper letters")
        print(f"{self.category_count['lower_case']} lower letters")
        print(f"{self.category_count['punctuation']} punctuation marks")
        print(f"{self.category_count['spaces']} spaces")
        print(f"{self.category_count['digits']} d")


def main():
    try:
        assert 2 == len(sys.argv)

        analyzer = TextAnalyzer(sys.argv[1])
        analyzer.report()

    except AssertionError as e:
        print(AssertionError.__name__ + ": wrong number of arguments.")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
