import sys

def mapper():
    for line in sys.stdin:
        article_id, cleaned_text = line.strip().split(",", 1)  
        words = cleaned_text.split()
        word_count = len(words)
        word_freq = {}
        for word in words:
            word_freq[word.lower()] = word_freq.get(word.lower(), 0) + 1
        
        for word, freq in word_freq.items():
            print(f"{word}\t{article_id}\t{freq}/{word_count}")

if __name__ == "__main__":
    mapper()

