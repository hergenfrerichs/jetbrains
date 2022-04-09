from bs4 import BeautifulSoup
import requests
import string

url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'

r = requests.get(url)
if r:
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        if article.contents[3].contents[0].text.strip() == 'News':
            title = article.contents[1].contents[3].contents[1].text.strip()
            # print(title)
            # mytable = title.maketrans(' ', '_', string.punctuation + '’')
            mytable = title.maketrans(' ', '_', string.punctuation)
            title_2 = title.translate(mytable)
            # print(title_2)
            link = article.contents[1].contents[3].contents[1].a['href']
            # print('https://www.nature.com' + link)
            r_2 = requests.get('https://www.nature.com' + link)
            soup_2 = BeautifulSoup(r_2.content, 'html.parser')
            article_2 = soup_2.find('div', {'class': "c-article-body"}).text.strip()
            # print(article_2)
            my_file = open(title_2 + '.txt', 'w', encoding="utf8")
            my_file.writelines(article_2)
            my_file.close()
else:
    print('Failure')


