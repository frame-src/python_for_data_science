def function_example_zero ():
    print("Function from example_0")


def count_in_list (ltc : list, str_tc ) -> int:
    counter = 0
    for v in ltc:
        if v == str_tc:
            counter = counter + 1
    return counter 