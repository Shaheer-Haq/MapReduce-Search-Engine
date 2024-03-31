import sys

def reducer():
    current_doc = None
    doc_vector = {}
    query_words = set()
    query_word_count = 0
    
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("END_OF_QUERY"):
            continue
        
        parts = line.split("\t")
        if len(parts) == 2:
            word, count = parts
            query_word_count += int(count)
            query_words.add(word)
        else:
            doc_id, word, tfidf = parts
            if current_doc == doc_id:
                doc_vector[word] = float(tfidf)
            else:
                if current_doc:
                    relevance_score = calculate_relevance(doc_vector, query_words, query_word_count)
                    print(f"{current_doc}\t{relevance_score}")
                
                current_doc = doc_id
                doc_vector = {word: float(tfidf)}
    
    if current_doc:
        relevance_score = calculate_relevance(doc_vector, query_words, query_word_count)
        print(f"{current_doc}\t{relevance_score}")

def calculate_relevance(doc_vector, query_words, query_word_count):
    relevance_score = 0
    for word, tfidf in doc_vector.items():
        if word in query_words:
            relevance_score += tfidf
    
    return relevance_score / query_word_count

if __name__ == "__main__":
    reducer()

