def find_smallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]

    for i in range(1, len(arr)):
        if smallest < arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

print(selectionSort([1, 4, 5, 2]))
