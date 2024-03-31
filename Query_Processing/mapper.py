import sys

def mapper():
    query = sys.argv[1].lower()  # Assuming query is passed as argument
    query_words = query.split()
    query_word_count = len(query_words)
    
    for word in query_words:
        print(f"{word}\t1")
    
    print("END_OF_QUERY\t1")
    
    for line in sys.stdin:
        word, doc_id, tfidf = line.strip().split("\t")
        print(f"{doc_id}\t{word}\t{tfidf}")

if __name__ == "__main__":
    mapper()

