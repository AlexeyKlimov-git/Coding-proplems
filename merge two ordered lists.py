l1 = [0, 1, 4]
l2 = [2, 5, 6]

size1 = len(l1)
size2 = len(l2)

res = [0] * (size1 + size2)
i1, i2, ires = 0, 0, 0

while i1 < size1 and i2 < size2:
    if l1[i1] < l2[i2]:
        res[ires] = l1[i1]
        i1 += 1
        ires += 1
    else:
        res[ires] = l2[i2]
        i2 += 1
        ires += 1

while i1 < size1:
    res[ires] = l1[i1]
    i1 += 1
    ires += 1

while i2 < size2:
    res[ires] = l2[i2]
    i2 += 1
    ires += 1

print(res)


