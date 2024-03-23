#Assignment 2 - Text-Analysis-Project
#Xinjia Chen 

#Part 1: Harvesting text from the Internet

#Part 1.1 - Collecting News Data

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='c03922ea1fb64861898541397f37e708')

from datetime import datetime, timedelta 

end_date = datetime.now() 
start_date = end_date - timedelta(days=25) #As I am not on a paid plan, I only have access to datas far back as 2024-02-22

start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')
'I learned the code above where I calculated start_date and end_date dynamically based on the current date from ChatGpt '

articles = newsapi.get_top_headlines(q="bitcoin", #I am Chilean-born Chinese who spend 7 years living in Chile and plan to go back to Chile in the long run. Hence, I am interested in how well is its economy doing right now. 
                                  sources='bbc-news,the-verge',
                                  language='en',
                                  from_param=start_date_str,
                                  to=end_date_str,
                                  sort_by='relevancy')

for article in articles['articles']:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}\n")


#Part 2: Analyzing Your Text
    
#Part 2.1 - Data preprocessing 
'''
As I learned in AQM-2000, Data preprocesses is essential in various data-minning as it help to clear the noises of data, clean and prepare the text data for analysis.
I learned how to preprocess data in python through ChatGpt and learned how to use NLTK in this website:  https://spotintelligence.com/2022/12/21/nltk-preprocessing-pipeline/
'''

import nltk 
nltk.download('punkt')  # Tokenization. It splits the text into individual words or subwords
nltk.download('stopwords')  # Stopwords. These are the words that does not add significant value to the text, such as "a", "an" and "the". Removing them will help the program to analyze text more effiencitly 
nltk.download('wordnet')  # Lemmatization. It reduce a word to its root form, making it easier for the program to perform analyze

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def preprocess(text):
     tokens = word_tokenize(text) #Tokenizes the input text into individual words/tokens
     tokens = [word.lower() for word in tokens] #Lowercase the words 

     stopwords = nltk.corpus.stopwords.words("english") #this gets a set of English stopwords from NLTK 
     tokens = [word for word in tokens if word not in stopwords]#We use the list above to filter out stopwords
     tokens = [word for word in tokens if word.isalpha()] #Remove punctuation and numbers
     tokens = [lemmatizer.lemmatize(word) for word in tokens]#This line applies lemmatization to each token which coverts tham to its dictionary form that is better for analyzing 
     return ' '.join(tokens) #Joins the processed tokens back into a single string with spaces between words and returns it.

preprocessed_articles = []
for article in articles['articles']: #I was getting empty result before adding '['articles']' to this line. It was suggested by ChatGpt as it ensure that this mathch to my data structure which i ignored
     text_to_preprocess = article['description']
     if text_to_preprocess: #check whether article is not None or an empty sting or not
        preprocessed_text = preprocess(text_to_preprocess)
        preprocessed_articles.append(preprocessed_text)  #Add back to the empty list created
preprocessed_articles

#Part 2.2 - Convert text into TF-IDF matrix
'''
As skylearn is not suggested to use in this project, I will be clculate TF-IDF manually. TF-IDF is a statistical measure that evaluates how relevant a word is to a document in a collection of documents.Hence, it is very important to this project. 
'''
#I copied how to calculate TF-IDF from this website with some alteration so it fits my code: 
from collections import Counter
import math

def calculate_tf(document):
    # Tokenize the document and count occurrences of each word
    tf_dict = {}
    words = document.split()
    word_count = len(words)
    word_counts = Counter(words)
     # Calculate TF for each word
    for word, count in word_counts.items():
        tf_dict[word] = count / float(word_count)
    return tf_dict

def calculate_idf(documents):
    import math
    N = len(documents)
    
    # Flatten all words in all documents
    all_words = set(word for document in documents for word in document.split())
    
    idf_dict = {}
    for word in all_words:
        containing_docs = sum(1 for document in documents if word in document.split())
        idf_dict[word] = math.log(N / containing_docs)
        
    return idf_dict

def calculate_tfidf(documents):
    # First, calculate the TF for each document
    tfs = [calculate_tf(doc) for doc in documents]
    
    # Calculate IDF using all documents
    idfs = calculate_idf(documents)
    
    # Combine TF and IDF to calculate TF-IDF
    tfidf_documents = []
    for tf in tfs:
        tfidf = {}
        for word, val in tf.items():
            tfidf[word] = val * idfs[word]
        tfidf_documents.append(tfidf)
    return tfidf_documents

tfidf_scores = calculate_tfidf(preprocessed_articles)
print(tfidf_scores)

#Part 2.3 - Clustering Articles

def simple_cluster_articles(tfidf_scores):
    clusters = {}
    for index, article_tfidf in enumerate(tfidf_scores):
        # Find the word with the highest TF-IDF score in each article
        top_word = max(article_tfidf, key=article_tfidf.get)
        if top_word not in clusters:
            clusters[top_word] = []
        clusters[top_word].append(index)  # Store index or title of the article
    return clusters

clusters = simple_cluster_articles(tfidf_scores)

def aggregate_tfidf_scores(tfidf_scores):
    # Aggregate TF-IDF scores for each word across all documents
    aggregated_tfidf = {}
    for article_tfidf in tfidf_scores:
        for word, score in article_tfidf.items():
            if word in aggregated_tfidf:
                aggregated_tfidf[word] += score
            else:
                aggregated_tfidf[word] = score
    return aggregated_tfidf

# Aggregate TF-IDF scores from all articles
aggregated_tfidf = aggregate_tfidf_scores(tfidf_scores)

# Sort words by their aggregated TF-IDF score in descending order
sorted_tfidf = sorted(aggregated_tfidf.items(), key=lambda item: item[1], reverse=True)

# Print the top 10 most important words
print("Top 10 Most Important Words Based on TF-IDF Scores:")
for word, score in sorted_tfidf[:10]:
    print(f"{word}: {score:.5f}")
