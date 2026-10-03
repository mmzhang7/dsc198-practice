def product_except_self(nums):
    res = [1] * len(nums)
    product_going_right = 1
    for i in range(len(nums)):
        res[i] = product_going_right
        product_going_right *= nums[i]
    product_going_left = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= product_going_left
        product_going_left *= nums[i]
    return res

assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
assert product_except_self([0, 4, 0]) == [0, 0, 0]
assert product_except_self([2, 5]) == [5, 2]


# The time complexity is O(N). The space complexity is O(1) 
# At first, I was thinking to use an on and off system for each index and multiplying through like linear algebra matrix but that would be O(N^2). I changed my method to only loop through twice, which still simplifies to O(N).