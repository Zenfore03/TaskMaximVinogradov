def combine_anagrams(words_array):
    anagram = {}
    for word in words_array:
        key = ''.join(sorted(word.lower()))
        if key not in anagram:
            anagram[key] = []
        anagram[key].append(word)
    return list(anagram.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))