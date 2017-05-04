from __future__ import unicode_literals
import utils
from brain import Memory


class Ear(object):
    """
    A simple ear that allows ChatterBot to
    communicate through the terminal.
    """
    @staticmethod
    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        user_input = utils.input_function()
        return Memory(user_input)
