from test_tools import *
from solved import *


def A(n):
    var = "and you "
    return "You " + n * var + "are fired!"

def B(m):
    var = "really "
    return "I am " + m * var + "furious."

def simplify(tweet):
    tweet = tweet.replace('FIRE', 'A')
    tweet = tweet.replace('FURY', 'B')
    for char in tweet:
        if char != 'A' and char != 'B': tweet = tweet.replace(char, '')
    return tweet

def transform(tweet):
    tweet = simplify(tweet)
    print(tweet)
    resp = ''
    for element in tweet:
        i = tweet.index(element)
        a = 0
        b = 0
        if tweet[i-1] == tweet[i]:
            if str(tweet[i]) == 'A':
                a += 1
            elif str(tweet[i]) == 'B':
                b += 1
        else: resp = resp + A(a) + B(b)

    return resp

print(transform('HALAHALAHALA'))
