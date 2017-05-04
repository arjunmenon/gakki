from __future__ import unicode_literals
from . import utils
from .ear import Ear

class ChatterBot(object):
    """
    A chat bot. 
    """
    def __init__(self):
        self.name = 'Gakki'
        self.languages = ['English']
        self.conversations = []

    def listen(self):
        self.conversations.append(Ear.process_input())

    def speak(self):
        pass

    def think(self):
        pass



