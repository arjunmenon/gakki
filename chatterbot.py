from __future__ import unicode_literals
from . import utils


class ChatterBot(object):
    """
    A chat bot. 
    """
    def __init__(self):
        self.name = 'Gakki'
        self.languages = ['English']
        self.conversations = []

    def listen(self):
        self.conversations.append(utils.input_function())

    def speak(self):
        pass

    def think(self):
        pass



