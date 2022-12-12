# f([1, 1, 0, 1, 1, 1]) = 3
# f([0, 0, 0]) = 0
# f([]) = 0
nums = [1, 1, 0, 1, 1, 1]


def foo(bin_list):
    current = 0
    best = 0
    for num in bin_list:
        if num > 0:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


print(foo(nums))
print(foo([]))
