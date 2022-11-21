q = [1, 3, 5, 8, 10, 13, 18, 36, 36, 78]
sortedQ = []

for i in range(len(q)):
    if i % 2 == 0 and q[i] % 2 == 0:
        sortedQ.append(q[i])

print('Liste sortiert:', sortedQ)
