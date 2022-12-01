# yield is return of generator
# but generator doesnt end at yield he only pass execution to another function and not end like return!!!

def haf():
    yield 1
    yield 2
    yield 3
    yield 4

# print(list(haf()))

for x in haf():
    print(x)
    if x >2:
        break