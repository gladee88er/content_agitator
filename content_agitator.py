from newspaper import Article
import nltk
from textblob import TextBlob
from bs4 import BeautifulSoup
import requests

print('Welcome to my news scraper bitches!')

# create an article object
article = Article('https://blog.finxter.com/newspaper3k-a-python-library-for-fast-web-scraping/')
article.download()
article.parse()
article.nlp()
title = article.title
link = article.url
authors = article.authors
date = article.publish_date
image = article.top_image
summary = article.summary
text = article.text
blob = TextBlob(text)
polarity = blob.sentiment.polarity

print('**********************************')
print(f'Title: {title}')
print(f'Link: {link}')
print(f'Author: {authors[0]}')
print(f'Publish Date: {date}')
print(f'Top Image: {image}')
print(f'Summary: ')
print(summary)
print()
if polarity > 0:
    print('The article is positive.')
elif polarity < 0:
    print('The article is negative.')
else:
    print('The article is neutral.')
print('**********************************')

