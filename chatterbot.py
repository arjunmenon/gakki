from __future__ import unicode_literals
from . import utils
from ear import Ear
from mouth import Mouth


class ChatterBot(object):
    """
    A chat bot. 
    """
    def __init__(self):
        self.name = 'Gakki'
        self.languages = ['English']
        self.conversations = []

    def listen(self, input_item, session_id=None):
        if not session_id:
            session_id = str(self.default_session.uuid)
        self.conversations.append(Ear.process_input(input_item))

    def speak(self, session_id=None):
        if not session_id:
            session_id = str(self.default_session.uuid)
        Mouth.process_input()

    def think(self):
        return self.trainer = training_class(self.storage, **kwargs)

    @classmethod
    def from_config(cls, config_file_path):
        """
        Create a new ChatBot instance from a JSON config file.
        """
        import json
        with open(config_file_path, 'r') as config_file:
            data = json.load(config_file)

        name = data.pop('name')

        return ChatterBot(name, **data)

