"""
CP1404 Practical 05
Word Occurrences Counter
Estimate: 25 minutes
Actual: 16
"""

def main():
    """Count and display word occurrences from user input string, sorted and aligned."""
    text = input("Text: ")

    words = text.split()

    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    unique_words = sorted(word_to_count.keys())

    max_length = max(len(word) for word in unique_words) if unique_words else 0

    for word in unique_words:
        print(f"{word:{max_length}}: {word_to_count[word]}")

main()