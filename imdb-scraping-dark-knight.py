import csv
import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

DOWNLOAD_URL = 'https://www.imdb.com/title/tt0468569/reviews?ref_=tt_urv'


def download_page(url):

    return urllib.request.urlopen(url)

# print(download_page(DOWNLOAD_URL).read())


def parse_html(html):
    """
    Read the data from IMDB and append write a csv. Also add a "sentiment" column that shows the overall sentiment of each review 
    """
    soup = BeautifulSoup(html, features="lxml")
    movie_table = soup.find('div', attrs={'class': 'lister-list'})
    review_list = []
    for divs in movie_table.find_all('div', attrs={"class": "lister-item mode-detail imdb-user-review collapsable"}):
        movie_rating = divs.find('div', attrs={'class': 'ipl-ratings-bar'})
        rating_container = movie_rating.find("span", attrs={'class': 'rating-other-user-rating'})
        rating_ratings = rating_container.find("span").text
        movie_review = divs.find('div', attrs={'class': 'content'})
        review_reviews = movie_review.find("div", attrs = {"class": "text show-more__control"}).text

        review_sentiment = SentimentIntensityAnalyzer().polarity_scores(review_reviews)
        if float(review_sentiment["compound"])>=0.05:
            sentiment = "Positive"
        elif float(j["compound"])<=-0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        review_list.append((review_reviews,rating_ratings, sentiment))
    return review_list



def main():
    url = DOWNLOAD_URL

    with open('dark_knight_movie_review.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        fields = ('reviews', 'ratings', 'sentiment')
        writer.writerow(fields)

        html = download_page(url)
        movies = parse_html(html)
        writer.writerows(movies)


if __name__ == '__main__':
    main()