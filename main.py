from test_tools import *
from solved import *


# def to_jaden_case(string):
#     string = string.replace('\'','')
#     string = string.title()
#     string = string.replace('Arent', 'Aren\'t')
#     return string

def divisor(num):
    l = []
    i = 1
    while i < num:
        if (num % i==0):
            l.append(i)
            i += 1
        else: i += 1
    return l

print(divisor(48))
print(divisor(75))


# if sum(a for a in divisor(strat)) == 1+ sum(b for b in divisor(limit)) or sum(b for b in divisor(limit)) == 1+ sum(a for a in divisor(strat)):
#     return ()
