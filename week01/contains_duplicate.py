def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


assert contains_duplicate([1, 2, 3, 1]) == True
assert contains_duplicate([]) == False
assert contains_duplicate([1, 2, 3, 4]) == False
assert contains_duplicate([1, 1, 1, 1]) == True

# The time complexity is O(N) and the space complexity is O(N), where N is the number of elements in the array.
# I first tried hashmaps, which didn't work as well since that data structure doesn't necessarily have unique keys, so I changed to a set, which only has unique values.
