from datetime import datetime

# Cleanin array diff
def array_diff(a, b):
    return [x for x in a if x not in b]

#Verifier si la date entrée en argument est bien la date d'aujourd'hui
def is_today(date):
    return date.date() == datetime.today().date()

# solution so that returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0

def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#capitalizing every word

def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())

# def to_jaden_case(string):
#     l = string.split()
#     for i in range(0, len(l)): l[i] = l[i].capitalize()
#     string = ' '.join(l)
#     return string
 

def sum_digits(number):
    x = str(abs(number))
    j = 0
    for i in x:
        j = int(j) + int(i)
    print(type(j))
    print(j)
    return j

#    return sum(int(d) for d in str(abs(number)))

# Buddy pairs
def div_sum(n):
    divs = set()
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)


def buddy(start, limit):
    for n in range(start, limit + 1):
        buddy = div_sum(n)

        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]

    return "Nothing"

# Clean a list from strings
def filter_list(l):
    return [x for x in l if not isinstance(x, str)]