import sys

def mapper():
    for line in sys.stdin:
        article_id, cleaned_text = line.strip().split(",", 1) 
        words = cleaned_text.split()
        unique_words = set(words)
        for word in unique_words:
            print(f"{word.lower()}\t1")

if __name__ == "__main__":
    mapper()

