from bs4 import BeautifulSoup
import os
import requests
import string


def url_builder():
    all_topics = []
    failed_topics = []
    # Input
    number_pages = int(input())
    # article_type = 'Nature Briefing'
    article_type = input()
    
    # Build url and start "save_text" function
    for i in range(1, number_pages + 1):
        url_input = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=' + str(i)
        # print(url_input)
        dir_name = 'Page_' + str(i)
        try:
            os.mkdir(dir_name)
        except Exception:
            print(dir_name + 'already exists')
        result = save_text(url_input, dir_name, article_type)
        all_topics.append(result[0])
        failed_topics.append(result[1])
    
    # Create sets and files of all topics, valid topics, failed topics
    all_topics_clean = [item for sublist in all_topics for item in sublist]
    failed_topics_clean = [item for sublist in failed_topics for item in sublist]
    
    #my_file_1 = open('all_topics.txt', 'w', encoding="utf8")
    #for item in sorted(set(all_topics_clean)):
        #my_file_1.writelines(item + '\n')
    #my_file_1.close()
    #my_file_2 = open('failed_topics.txt', 'w', encoding="utf8")
    #for item in sorted(set(failed_topics_clean)):
        #my_file_2.writelines(item + '\n')
    #my_file_2.close()
    #my_file_3 = open('valid_topics.txt', 'w', encoding="utf8")
    #for item in sorted(set(all_topics_clean) - set(failed_topics_clean)):
        #my_file_3.writelines(item + '\n')
    #my_file_3.close()
                             
  
def save_text(url, dir_input, article_input):
    # url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
    # Collect topics
    all_topics = []
    failed_topics = []
    # Run parsing function
    r = requests.get(url)
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            topic = article.contents[3].contents[0].text.strip()
            all_topics.append(topic)
            # print(topic)
            if article.contents[3].contents[0].text.strip() == article_input:
            # if article.contents[3].contents[0].text.strip():
                try:
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
                    try:
                        article_2 = soup_2.find('div', {'class': "c-article-body"}).text.strip()
                        # print(article_2)
                        my_file = open(dir_input + '/' + title_2 + '.txt', 'w', encoding="utf8")
                        my_file.writelines(article_2)
                        my_file.close()
                    except Exception:
                        print(f'Exception: {topic} {link}')
                        failed_topics.append(topic)
                except Exception:
                    print(f'Exception: {topic}')
                    failed_topics.append(topic)
        return all_topics, failed_topics
    else:
        print('Failure')


url_builder()
    
