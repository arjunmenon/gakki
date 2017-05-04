from __future__ import unicode_literals
import utils
from brain import Memory


class Mouth(object):
    """
    A simple Mouth that allows ChatterBot to
    communicate through the terminal.
    """
    def __init__(self):
        self.user_output = []
        if len(Memory.output_conversations) > 0:
            self.user_output.append(Memory.output_conversations.pop())


    def process_input(self, *args, **kwargs):
        """
        Output the bot's input to the terminal.
        """
        self.user_output = utils.output_function(self.user_output)
        return self.user_output

