import sys

def mapper():
    for line in sys.stdin:
        ARTICLE_ID, cleaned_text = line.strip().split(",", 1) 
        words = cleaned_text.split()
        for word in words:
            print(f"{word.lower()}\t1")

if __name__ == "__main__":
    mapper()

