def valid_palindrome(s):
    l, r = 0, len(s)-1
    while l < r:
        while l<r and not s[l].isalnum():
            l+=1
        while l<r and not s[r].isalnum():
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l+=1   
        r-=1
    return True


# Time complexity is O(N), space complexity is O(1)
# The first time I approached this, I forgot to write whe while l<r within the second while loop. I also forgot to add the increments to l and r outside of the loop.