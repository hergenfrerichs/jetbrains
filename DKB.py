from bs4 import BeautifulSoup
import requests

base_url = 'https://jobs.dkb.de/go/Berufserfahrene/3841701/'

base_list = [base_url]

index = 0
for i in range(1, 8):
    index = i * 25
    base_list.append(base_url + str(index))

test = base_list[1]

for entry in base_list:
    r = requests.get(entry)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find_all('a', 'jobTitle-link')
    for i in title:
        i = i.text
        print(i)

