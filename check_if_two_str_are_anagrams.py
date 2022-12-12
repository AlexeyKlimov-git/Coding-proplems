def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    if freq1 != freq2:
        return False
    return True

s1='adf'
s2='fas'

print(are_anagrams(s1, s2)) # T ~ O(n), S ~ O(n)

# 2nd way - can use Collections, T ~ O(n), S ~ O(n)
# 3d way - can use sorted(), T ~ O(nlogn), S ~ O(n)


