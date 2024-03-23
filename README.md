# Text-Analysis-Project
 
#1 - Project Overview
In this text analysis project, I leveraged the News API to harvest news articles related to specific keywords, and in the end this program will print out Top 10 Most Important Words Based on TF-IDF Scores. To process and analyze the harvested text, I utilized Natural Language Processing (NLP) techniques, including tokenization, stop word removal, lemmatization, and TF-IDF (Term Frequency-Inverse Document Frequency) calculation. These methods allowed for the cleaning and preparation of text data, making it suitable for further analysis. By calculating TF-IDF scores, I aimed to identify the most relevant words within the articles, providing insights into the predominant themes and topics of discussion.  

#2 - Implementation
This project's architecture is mainly based on three main part: data collection, text preprocessing and text analysis. 

At the project'sincepetion, we use the News APi to retrive articles centered around the key word that the user desire to know more about. After we finished collecting data, we need to preprocess the text so that is could be used for analyszing. This stage involves several steps: tokenization (splitting text into words), converting to lowercase, removing stopwords (common words that add little value to analysis), removing non-alphabetic characters, and lemmatization (reducing words to their base or dictionary form). The NLTK library supports these operations, offering a comprehensive toolkit for text processing. This preprocessing step is critical for reducing noise in the data and ensuring that the analysis focuses on meaningful content. 

The essence of the analysis involved the manual computation of TF-IDF (Term Frequency-Inverse Document Frequency) scores for the text that had been prepared through preprocessing. This statistical approach is utilized to gauge the relevance of words within the documents in comparison to the overall corpus. The process entailed the development of functions to calculate both the term frequency (TF) and the inverse document frequency (IDF), which were then integrated to ascertain the TF-IDF scores for every word across the documents. Subsequently, these scores were applied to group articles and pinpoint predominant themes, using a straightforward clustering method that selects the highest TF-IDF score per article as its basis.

In this exploratory endeavor, ChatGPT was instrumental, functioning as both an advisor and collaborator. It provided clarity on navigating through the complexities of natural language processing (NLP) techniques, delivered insightful advice on the implementation of algorithms, and served as a platform for troubleshooting and refining ideas. One of the key function of ChatGpt for me is its debugging ability. Whenever I have a bug in my function and I cannot find it, I can put it in GPT and let it help me to solve my problem. This interaction underscores the potential of artificial intelligence to facilitate the research process, augmenting the researcher's capacity to explore and interpret complex data landscapes.

#3 - Results

The outcomes of the project, particularly in terms of the analysis of articles related to "Chile" and "Economy," were not entirely satisfactory. Utilizing the program to search these keywords yielded a list of the top 10 most significant words based on their TF-IDF scores: 
;;Top 10 Most Important Words Based on TF-IDF Scores:
say: 3.30821
economy: 2.88507
budget: 2.65775
minister: 2.43443
first: 2.37346
year: 2.33431
could: 2.27641
tax: 2.07460
election: 2.03673
chancellor: 2.01826;;

This outcome prompts a critical reflection on the project's methodology, specifically the effectiveness of TF-IDF scoring as a tool for extracting meaningful insights from news articles. The inclusion of common terms in the list of top words indicates a potential need for further refinement in the preprocessing stage, such as more aggressive filtering of generic terms or the incorporation of more sophisticated contextual analysis techniques.

Furthermore, the project's manual approach to calculating TF-IDF  might have contributed to the limitations in effectively identifying the most relevant themes. Exploring alternative or more advanced natural language processing techniques could provide deeper insights into the thematic structures of the corpus.

Yet, it is still some what useful. For example when I search techonology, I get ai as the second most important word, which is somewhat interesting. 

#4 Reflection 

In working on this project, I took a step-by-step approach, starting from gathering data, moving on to cleaning it up, and finally analyzing it to find patterns or important insights. This method worked out pretty well because it kept things organized and allowed me to focus on one part of the problem at a time. However, I think I was a bit optimistic about what I could achieve with the tools and techniques I chose, especially when it came to analyzing the text data. My plan for testing how well the analysis worked could also have been better; it would have been helpful to try out the process on different kinds of text to see if I could consistently get useful results.

Through this experience, I learned a lot about processing and analyzing text data, which was the main goal. ChatGPT was a big help here. It was like having a knowledgeable friend who could immediately give me advice, suggest new ways to tackle a problem, or help me understand complex ideas better. This back-and-forth with ChatGPT made learning faster and more interesting. Moving forward, I'll definitely use what I've learned about analyzing text and working with natural language processing in future projects. It's clear now that having a solid understanding of more advanced analysis techniques and machine learning could have made my project even better. Knowing how to blend these more sophisticated methods with the basics I started with will be my takeaway for next time, aiming for an approach that's both deep and broad to get sharper insights from the data.