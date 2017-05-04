from . import preprocessors


class Memory(object):
    """
    Class memory will processing one statement and store it 
    """
    conversations = []

    def __init__(self, text, **kwargs):

        # Try not to allow non-string types to be passed to statements
        try:
            self.text = str(text)
        except UnicodeEncodeError:
            pass

        self.text = preprocessors.pre_process(self.text)
        Memory.conversations.append(self.text)

    def __str__(self):
        return self.text

    def __repr__(self):
        return '<Statement text:%s>' % (self.text)

    def __hash__(self):
        return hash(self.text)

    def __eq__(self, other):
        if not other:
            return False

        if isinstance(other, Memory):
            return self.text == other.text

        return self.text == other

