candidates = range(134564, 585159)

def bonkers(number):
    (a,b,c,x,y,z) = list(str(number))
    foo = a == b != c
    bar = a != b == c != x
    baz = b != c == x != y
    qux = c != x == y != z
    quz = x != y == z
    return foo or bar or baz or qux or quz

def ordered(number):
    str_rep = str(number)
    return list(str_rep) == sorted(str_rep)

def duplicative(number):
    str_rep = str(number)
    return any([x == y for x,y in zip(str_rep, str_rep[1:])])

usable = filter(ordered, candidates)
usable = filter(duplicative, usable)
usable = filter(bonkers, usable)

usable = list(usable)
print(len(usable))