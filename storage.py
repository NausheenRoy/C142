import csv

from main import liked_article, unliked_article

all_articles = []

with open('articles.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_article = []
unliked_article = []
