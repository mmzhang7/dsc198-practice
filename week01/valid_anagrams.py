def is_anagram(s, t):
    if len(s) != len(t):
        return False
        
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    for char in t:
        if counts.get(char, 0) == 0:
            return False
        counts[char] -= 1
        
    return True

assert is_anagram("anagram", "nagaram") == True
assert is_anagram("a", "ab") == False
assert is_anagram("rat", "car") == False
assert is_anagram("", "") == True

# The time complexity is O(N), where N is the length of the strings. The space complexity is O(1) because the hash map size is bounded by the 26 lowercase English letters.
# The least efficient way that I thought of at first was just sorting both arrays and comparing them to each other, but that takes sorting time complexity/ Intuitively, there should be a different way to use a hash map to keep things organized.