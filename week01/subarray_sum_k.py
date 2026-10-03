def subarray_sum(nums, k):
    count = 0
    current_sum = 0
    prefix_sums = {0: 1} 
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
    return count



assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([], 0) == 0
assert subarray_sum([0, 0, 0], 0) == 6
assert subarray_sum([1, -1, 1, 1, -1, -1], 0) == 6
assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4
assert subarray_sum([1, 2, 3], 10) == 0

# Time complexity = O(N) to go through the array once, and space complexity = O(N) to create the hashmap.
# On the first try, I forgot to account for the first step and initiated the hashmap sums differently. The second approach I tried fixed the edge cases.