import requests

from bs4 import BeautifulSoup


letter = 'S'
url = input()

def subtitle(my_input):
    result = []
    r = requests.get(my_input)
    soup = BeautifulSoup(r.content, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        if len(i.text) > 1 and i.text.startswith(letter):
            if 'topics' in i.get('href') or 'entity' in i.get('href'):
                result.append(i.text)

    print(result)

subtitle(url)



