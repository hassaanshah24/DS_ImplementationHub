from collections import Counter

def word_count(sentence):
    words = sentence.split()
    return Counter(words)

# Example usage
if __name__ == "__main__":
    sentence = "apple banana apple orange banana apple"
    print("Word Frequency:", word_count(sentence))
