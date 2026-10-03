def group_anagrams(words):
    groups = {}
    for w in words:
        counts = [0] * 26
        for ch in w:
            counts[ord(ch) - ord("a")] += 1
        key = tuple(counts)
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return list(groups.values())

# Time complexity is O(N*K) and space complexity is O(N*K) where N is the number of strings and K is the max length of any string in the array.
# First, I tried a sorting method that sorted the strings alphabetically. However, per the method discussed in class, it is more optimal to hash map with character frequency count array as the key.