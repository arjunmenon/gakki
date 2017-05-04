# -*- coding: utf-8 -*-
import re
import unicodedata
import sys


def __clean_whitespace(text):
    """
    Remove any consecutive whitespace characters from the text.
    """
    # Replace linebreaks and tabs with spaces
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

    # Remove any leeding or trailing whitespace
    text = text.strip()

    # Remove consecutive spaces
    text = re.sub(' +', ' ', text)

    return text


def __convert_to_ascii(text):
    """
    Converts unicode characters to ASCII character equivalents.
    For example: "på fédéral" becomes "pa federal".
    """

    # Normalize unicode characters
    if sys.version_info[0] < 3:
        text = unicode(text) # NOQA

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')

    text = str(text)
    return text


def __remove_noise(text):
    """    
    :param text: 
    :return: noise_free_text
    """
    # may update in the future
    noise_list = ["is", "a", "this", "..."]
    words = text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    text = " ".join(noise_free_words)
    return text
