number_pages = int(input())
for i in range(1, number_pages + 1):
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=' + str(i)
    print(url)
