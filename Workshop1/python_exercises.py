"""
Intro to python exercises shell code
"""

def is_odd(x):
    if x % 2 == 0:
        return True
    return False
    """
    returns True if x is odd and False otherwise
    """

def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            return False
    return True
    """
    returns whether `word` is spelled the same forwards and backwards
    """

def only_odds(numlist):
    oddList = []
    for elt in numList:
        if elt % 2 == 1:
            oddList.append(elt)
    return oddList
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    Dict = {}
    textList = text.split()
    for txt in textList:
        txt.lower()
        if txt in Dict:
            Dict[txt] += 1
        else:
            Dict[txt] = 1
    return Dict
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
