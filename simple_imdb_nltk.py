import csv
from textblob import TextBlob
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.corpus import stopwords
nltk.download("stopwords")
from nltk.classify import SklearnClassifier

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

# from subprocess import check_output


with open('dark_knight_movie_review.csv', 'r') as csvfile:
    """
    Open the file and run sentiment analysis through each review
    """

    readCSV = csv.reader(csvfile) #delimiter = ' '
    # print(readCSV)
    # for row in readCSV:
    #     sentence = row[0]
    #     blob = TextBlob(sentence)
    #     score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    #     print(score, blob.sentiment)

    sentiments = [[SentimentIntensityAnalyzer().polarity_scores(row[0]), TextBlob(row[0]).sentiment] for row in readCSV]
    # print(type(sentiments[0][1]))
    for items in sentiments:
        """
        printing each sentiment analysis line by line
        """
        print(items)

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets

csv_file = "C:/Users/cngo1/Documents/GitHub/text-mining/dark_knight_movie_review.csv"
data = pd.read_csv(csv_file)


data = data[['reviews','sentiment']]

# Splitting the dataset into train and test set
train, test = train_test_split(data,test_size = 0.3)
# Removing neutral sentiments
"""
Clear the data of any neutral reviews
"""
train = train[train.sentiment != "Neutral"]

"""
Train each positively reviewed data
"""
train_pos = train[train['sentiment'] == 'Positive']
train_pos = train_pos['reviews'] 


# train_neg = train[train['sentiment'] == 'Negative']
# train_neg = train_neg['reviews']

# stopwords_list = ["Heath Ledger", "movie", "Dark", "Knight", "Joker", "the", "Batman", "Christopher Nolan"]


def wordcloud_draw(data, color='black'):
    """
    Creating the wordcloud, its dimensions and colors 
    """
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()])
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color=color,
                          width=2500,
                          height=2000
                          ).generate(cleaned_word)
    plt.figure(1, figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

# print("Positive words")
wordcloud_draw(train_pos, 'white') 
# # print("Negative words")
# # wordcloud_draw(train_neg)


   

