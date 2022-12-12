j = 'ab'
s = 'aabbccd'

result = 0
for ch in s:
    if ch in j:
        result += 1

print(result)