x = ['ab', 'cd']
print(list(map(list, x)))

# map(fun, iter)
# fun ist eine Funktion die durch die iterierbaren Elemente geht
# iter ist eine iterable die gemappt wird
# list() sorgt dafür, dass die iterablen in eine Liste gecasted werden
