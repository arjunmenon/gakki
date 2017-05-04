from __future__ import unicode_literals
import utils


class Ear(object):
    """
    A simple ear that allows ChatterBot to
    communicate through the terminal.
    """

    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        user_input = utils.input_function()
        return Memory(user_input)
