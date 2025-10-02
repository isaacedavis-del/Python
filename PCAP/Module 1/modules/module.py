#!/usr/bin/env python3 

""" module.py - an example of a Python module """

__counter = 0

def suml(the_list):
    # sourcery skip: inline-immediately-returned-variable, simplify-generator, sum-comprehension
    """Calculates the sum of all elements in a list.
    
    This function takes a list of numbers and returns their sum.

    Args:
        the_list: A list of numeric elements to be summed.

    Returns:
        The sum of all elements in the_list.
    """
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    """Calculates the product of all elements in a list.

    This function takes a list of numbers and returns their product.

    Args:
        the_list: A list of numeric elements to be multiplied.

    Returns:
        The product of all elements in the_list.
    """
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)