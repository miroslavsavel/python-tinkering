a = ['first', 'second', 'third']

itr = iter(a)

print(next(itr))
print(next(itr))
print(next(itr))


d = {'foo' : 1, 'bar': 2, 'baz': 3}

for k in d:
    print(k)