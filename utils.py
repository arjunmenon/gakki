from __future__ import print_function


def input_function():
    """
    Normalizes reading input between python 2 and 3.
    The function 'raw_input' becomes 'input' in Python 3.
    """
    import sys

    if sys.version_info[0] < 3:
        user_input = str(raw_input())  # NOQA

        # Avoid problems using format strings with unicode characters
        if user_input:
            user_input = user_input.decode('utf-8')

    else:
        user_input = input()  # NOQA

    return user_input


def output_function(statement):
    """
    Normalizes output between python 2 and 3.
    """
    print(statement)
