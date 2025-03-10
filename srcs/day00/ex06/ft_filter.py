from typing import Generator


def ft_filter(function, iterable) -> Generator:
    """
        Apply the function to each value of an iterable object
        Returns a list of objs for which the function returns True;
    """
    if iterable:
        for value in iterable:
            if function(value):
                yield (value)
