# MapReduce-Search-Engine
## Introduction

This report outlines the development of a basic search engine using Apache Hadoop's MapReduce Framework. The Search engine is designed to index a large corpus of csv document and process queries to retrieve relevant Documents efficiently. The implementation follows the principles of the Vector Space Model and utilizes TF/IDF weights for document representation and relevance calculation.

## Project Structure

The project is organized into several components:

1. **Data Preprocessing:** The initial step involves cleaning and processing the input text data. This includes tokenization, removing stop words, and converting text to lowercase.

2. **Indexing:** The indexing phase consists of mapping terms to unique IDs, calculating TF/IDF weights for each document, and generating an index for efficient retrieval.

3. **Query Processing:** Given a query, the system generates a vector representation based on TF/IDF weights and calculates the relevance scores between the query and documents in the index.

4. **Ranking:** The documents are ranked based on their relevance scores, and the top results are returned to the user.

## Implementation Details

**Data Preprocessing**
1. **Tokenization:** We use a simple tokenizer to split text into individual terms.
2. **Stop Words Removal:** Common stop words are removed to reduce noise in the index.
3. **Lowercasing:** Text is converted to lowercase to ensure case-insensitive matching.

**Indexing**

1. **Word Enumeration:** This MapReduce task scans the corpus, generates a set of unique words, and assigns a unique ID to each word.

2. **Document Count:** Another MapReduce task calculates the Inverse Document Frequency (IDF) for each term, representing the number of documents in which a term appears.

3. **Indexer:** For each document, the Indexer computes the TF/IDF representation and stores it in the index along with the document ID.

**Query Processing**

1. **Query Vectorizer:** Given a query, this function generates a vector representation based on TF/IDF weights calculated during indexing.

2. **Relevance Analizator:** Calculates the relevance scores between the query vector and document vectors using the inner product.

**Ranking**
1. The Ranker Engine sorts the documents based on their relevance scores and returns the top results to the user.

**Results and Performance**

1. The search engine was tested on a subset of the English Wikipedia dump containing approximately 100,000 articles.

2. Initial indexing of the corpus took several hours due to the large dataset size.

3. Query processing and document retrieval were performed efficiently, with most queries returning relevant results within milliseconds.


## Conclusion

In conclusion, the developed search engine demonstrates the effectiveness of using Apache Hadoop's MapReduce framework for indexing and retrieving documents from a large text corpus. By implementing the Vector Space Model and TF/IDF weighting, the system efficiently processes queries and returns relevant results to the user.

## Contributors

1. Moeez Ahmed Khan: 21i-1694
2. Meeran Ali: 21i-1743
3. Shaheer-E-Haq: 21i-1657
