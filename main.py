from test_tools import *
from solved import *
# def to_jaden_case(string):
#     string = string.replace('\'','')
#     string = string.title()
#     string = string.replace('Arent', 'Aren\'t')
#     return string

def buddy(start, limit):
    def divisor(num):
        divisors = []
        i = 1
        while i < num:
            if num % i:
                divisors.append(i)
                i+=1
        return divisors

    if sum(a for a in divisor(strat)) == 1+ sum(b for b in divisor(limit)) or sum(b for b in divisor(limit)) == 1+ sum(a for a in divisor(strat)):
        return ()
