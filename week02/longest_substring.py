def lengthOfLongestSubstring(self, s: str) -> int:
    length = 0
    l = 0
    seen = set()
    for r in range(0,len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l +=1
        seen.add(s[r])
        length = max(length, r-l+1)
    return length