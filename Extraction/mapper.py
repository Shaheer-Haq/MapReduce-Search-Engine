import sys

def mapper():
    relevant_ids = set(sys.argv[1:])  
    
    for line in sys.stdin:
        ARTICLE_ID, cleaned_text = line.strip().split(",", 1)  
        if article_id in relevant_ids:
            print(f"{article_id}\t{section_text}")

if __name__ == "__main__":
    mapper()

