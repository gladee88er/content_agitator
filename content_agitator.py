#  This new code changes the design of the program by defining a function scrape_arlicle that can be used to help with future expansion of functionality. 
#  Also the ability to scrape multiple URL;s has been added.

from newspaper import Article
from textblob import TextBlob

def scrape_article(url):
    article = Article(url)
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

urls = ['https://www.askpython.com/python-modules/nltk-punkt', 'https://blog.finxter.com/newspaper3k-a-python-library-for-fast-web-scraping/']

for url in urls:
    scrape_article(url)


