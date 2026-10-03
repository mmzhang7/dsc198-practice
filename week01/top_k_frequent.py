def top_k_frequent(nums, k):
    count = {}
    for v in nums:
        count[v] = count.get(v,0)+1  
    buckets = [[] for _ in range(len(nums) + 1)]
    for v, c in count.items():
        buckets[c].append(v)
    out = []
    for c in range(len(nums), 0, -1):
        for v in buckets[c]:
            out.append(v)
            if len(out) == k:
                return out
    return out


assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    
# Boundary: Single element
assert set(top_k_frequent([1], 1)) == {1}
    
# Boundary: Negative numbers
assert set(top_k_frequent([-1, -1, -1, -2, -2, 3], 2)) == {-1, -2}
    
# Boundary: Multiple elements with the same frequency
assert len(top_k_frequent([1, 2, 3, 4], 2)) == 2

# The time complexity is O(N) and the space complexity is O(N), where N is the number of elements in the array.

# First, I initially considered counting the frequencies in a hash map then sorting the unique elements based on those counts. However, this failed to meet the optimal efficiency constraints because standard sorting results in an O(N log N) time complexity. Then, I shifted to a bucket sort approach as discussed in class.