from datetime import datetime


class Memory(object):
    """
    Class memory will processing one statement and store it 
    """

    def __init__(self, text, **kwargs):

        # Try not to allow non-string types to be passed to statements
        try:
            text = str(text)
        except UnicodeEncodeError:
            pass

        text = preprocess(text)
