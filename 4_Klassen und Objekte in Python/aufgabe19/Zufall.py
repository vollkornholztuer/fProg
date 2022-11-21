import time

m = 32768
b = 9757
c = 6925

firstCall = False


def rand(a=int(time())):
    while True:
        a = (a * b + c) % m
        yield a


def randDouble():
    random = rand()
    while True:
        yield next(random) / m


r = randDouble()
for i in range(10):
    print(next(r))
