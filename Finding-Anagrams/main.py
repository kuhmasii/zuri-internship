# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    check_ana =  all(list(map(lambda x : x in word, anagram)))
    if check_ana:
        return True
    return False

find_anagram("hello", "check")
find_anagram("below", "elbow")