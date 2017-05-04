# Gakki

Gakki is a mixed architecture chat bot. It was designed to simulate conducting dialogues with humans. 

An example of typical input would be some thing like this:

> **user:** Hello  
> **Gakki:** Hi there!  
> **user:** Good morning! How are you doing?  
> **Gakki:** I am working on the HCI homework, thank you for asking.  
> **user:** How is your candidacy exam?  
> **Gakki:** I failed it!  

## Goal
I have designed and implemented the Gakki, a chat bot to conducts a conversation via text.
Gakki shares many of the same goal as previous chat bot. However, its design has been driven
some limitations of existing chat bots like ELIZA, ALICE, XiaoIce. I have reflected traditional
choices and explored radically different points in the design space.
### Personification
Current chat bots are either Rule-based or Corpus-based. For both of them, they are just some
mixed regular expressions, parsers or complicated machine learning algorithms. Inspired
by cognitive science, I was wondering if I could imitate how human minds work. I try to
name part the corresponding name in human body, which increases code's readability and abstraction
level.
### Simple
I don't have time to write a complicated chat bot. Also, I don't expect the chat bot to 
speak many languages or serve various goals and purposes. Apart from designs, its implementation
also should be as simple. For example, I don't need to re-implement some deep learning 
library.
### Mixed Model
Existing chat bots are either rules-based or corpus-based. Rule-based models are good at handling
situations which were defined before. But every rules need to be pre-defined before. Corpus-based
model typically use deep learning to predict the next sentence. However, it need to be trained 
before. For some sentence like "What is the time", the accuracy won't increase even prolong
the training time.

## Design Overview
This part will introduce three main components of Gakki.
![Chatterbot: Machine learning in Python](https://github.com/callmeshabi/gakki/blob/master/figure/archit.png)
### Architecture
#### Mouth and Ear
Mouth is the first component of the chat bot. It basic function is to get input from terminal,
After that, it will preprocess the input and store it in the Memory.
##### 1. CLean whitespace and Convert to ASCII
The first step is to any consecutive whitespace characters from the text and Converts unicode characters to 
ASCII character equivalents.
##### 2. Remove Noise
Any text that is independent of the data context and the final output can be sentenced to noise.
The general practice of removing noise is to prepare a dictionary of noise entities, one by one on the text object (or 
word by word) iteration, to eliminate the noise dictionary appears in the label.

Here is the python code:
~~~~
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
~~~~
#### 3. Standard text
Text data often contains words or phrases that do not appear in any standard dictionary. Both search engines and models
can not recognize these.

For example, acronyms, vocabulary labels and popular slang. This type of noise can be repaired by regular expressions 
and manually prepared data dictionaries. The following code uses the dictionary lookup method to replace the social 
slang in the text.

Here is the python code:
~~~~
def __lookup_words(text):
    words = text.split() 
    new_words = [] 
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        new_words.append(word) new_text = " ".join(new_words) 
        return new_text
~~~~
Currently, the lookup_dict is from NLTK, a suite of libraries and programs for symbolic and statistical natural language
processing (NLP) 
#### Brain
### Discussions

## Related Work
### ChatterBot
### NLTK
## Future Work
This is [an example][id] reference-style link.

This is [an example](http://example.com/ "Title") inline link.
[id]: http://example.com/  "Optional Title Here"