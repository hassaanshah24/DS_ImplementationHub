from collections import Counter

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

# Example usage
if __name__ == "__main__":
    word1 = "listen"
    word2 = "silent"
    print(f"Are '{word1}' and '{word2}' anagrams?", is_anagram(word1, word2))  # Should return True

    word3 = "hello"
    word4 = "world"
    print(f"Are '{word3}' and '{word4}' anagrams?", is_anagram(word3, word4))  # Should return False
