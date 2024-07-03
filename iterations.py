i = [1, 2, 3]


""" list comprehensions """


def listComprehension(items):
    return [x * x for x in items if x % 2 != 0]


print(listComprehension(i))


""" generator """


def generator(items):
    return (x * x for x in items if x % 2 != 0)


for x in generator(i):
    print(x)


""" iter and next """


def iterAndNext(items):
    final = []
    x = iter(items)
    try:
        while True:
            final.append(next(x))
    except Exception:
        return final


print(iterAndNext(i))
