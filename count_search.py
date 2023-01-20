def count_sort(arr):

    # define max number of items in arr
    scope = max(arr) + 1

    # create list to store number of items
    C = [0] * scope

    # count items
    for x in arr:
        C[x] += 1

    # fill arr in ordered way
    arr = []
    for idx in range(scope):
        arr += [idx] * C[idx]
    return arr

# O(N+scope)

print(count_sort([2, 3, 1]))

