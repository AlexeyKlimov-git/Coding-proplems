# trick is to use three pointers Low, Mid and High
# idea is to move 0's to left and 2's to right of the array


# Step 1. Initialize value for Low, mid =0,0 , High=Len(nums) - 1
# Step 2.
# Case 1.
# Whenever nums[Mid] is 0 we should swap nums[Low] and nums[mid] and increment both pointers Low++, Mid++
# Case 2.
# Whenever nums[mid] is 2 we should swap nums[High] with nums[Mid] and decrement High --
# Case 3:
# If nums[mid] is 1 just increment mid++


nums = [0, 1, 1, 0, 2, 2, 0]

def sortColors(nums):
    low = 0
    high = len(nums) - 1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
        else:
            mid += 1
    return nums

print(sortColors(nums)) #O(n) time and O(1) space