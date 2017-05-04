from __future__ import unicode_literals
import utils
from brain import Memory


class Ear(object):
    """
    A simple ear that allows ChatterBot to
    communicate through the terminal.
    """
    def __init__(self):
        self.user_input = []

    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        self.user_input = utils.input_function()
        Memory(self.user_input)
        return self.user_input
