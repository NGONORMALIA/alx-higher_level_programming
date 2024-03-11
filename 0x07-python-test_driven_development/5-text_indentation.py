#!/usr/bin/python3
"""Module to print text with some intenetation
"""


def text_indentation(text):
    """to print full text

    Args:
        text: the text to print

    raises:
        TypeError:if text iis not a string
    """
    if (type(text) != str):
        raise TypeError("text must be a string")
    mystr = list(text)

    for word in range(len(mystr)):
        print("{}".format(mystr[word]), end="")
        if mystr[word] in ('.', ':', '?'):
            print("")
            mystr[word + 1] = "\n"
    print(text)
