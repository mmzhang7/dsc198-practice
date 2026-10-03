def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        if target-v in seen:
            return [seen[target-v],i]
        seen[v] = i
    return []

def test_two_sum():
    # Typical
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    # Empty
    assert two_sum([], 5) == []
    # Boundary: duplicate values
    assert two_sum([3, 3], 6) == [0, 1]
    # Boundary: negative numbers
    assert two_sum([-1, -2, -3, -4], -5) == [1, 2]
    # Boundary: no solution
    assert two_sum([1, 2, 3], 10) == []
    
# Time complexity is O(N), space complexity is also O(N).
# I haven't done DSA in a long time, so I needed some refreshers before approaching the problem. Then, I forgot to account for no solution/empty by writting the return [] at the end.