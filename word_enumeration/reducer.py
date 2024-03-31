import sys

def reducer():
    current_word = None
    word_count = 0
    
    for line in sys.stdin:
        word, count = line.strip().split("\t")
        if current_word == word:
            word_count += int(count)
        else:
            if current_word:
                print(f"{current_word}\t{word_count}")
            
            current_word = word
            word_count = int(count)
    
    if current_word:
        print(f"{current_word}\t{word_count}")

if __name__ == "__main__":
    reducer()

