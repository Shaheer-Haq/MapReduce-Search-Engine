import sys

def reducer():
    current_word = None
    postings_list = []
    
    for line in sys.stdin:
        word, doc_id, tfidf = line.strip().split("\t")
        if current_word == word:
            postings_list.append((doc_id, tfidf))
        else:
            if current_word:
                print(f"{current_word}\t{postings_list}")
            
            current_word = word
            postings_list = [(doc_id, tfidf)]
    
    if current_word:
        print(f"{current_word}\t{postings_list}")

if __name__ == "__main__":
    reducer()

