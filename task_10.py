import re

def count_words(string):
    string = string.lower()
    string = re.sub(r'[^a-z\s]', '', string)
    counts = {}
    for word in string.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))

