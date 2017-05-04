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

### Architecture
#### Brain
#### Mouth and Ear
### Discussions

## Related Work
### ChatterBot
### NLTK
## Future Work
This is [an example][id] reference-style link.

This is [an example](http://example.com/ "Title") inline link.
[id]: http://example.com/  "Optional Title Here"