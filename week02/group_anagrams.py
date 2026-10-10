def group_anagrams(words):
    groups = {}
    for word in words:
        vals = [0]*26
        for char in word:
            vals[ord(char)-ord("a")] +=1
        key = tuple(vals)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["listen","silent",'enlist','cat','act','dog'])) #, [["listen","silent","enlist"], ['cat','act'],['dog']]
print(group_anagrams([]))
        