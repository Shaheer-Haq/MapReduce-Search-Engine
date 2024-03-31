import sys

def reducer():
    current_word = None
    doc_count = 0
    
    for line in sys.stdin:
        word, count = line.strip().split("\t")
        if current_word == word:
            doc_count += int(count)
        else:
            if current_word:
                print(f"{current_word}\t{doc_count}")
            
            current_word = word
            doc_count = int(count)
    
    if current_word:
        print(f"{current_word}\t{doc_count}")

if __name__ == "__main__":
    reducer()

