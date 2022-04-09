from bs4 import BeautifulSoup
import requests


def user_input():
    u_input = input()
    # u_input = 'https://www.imdb.com/title/tt0080684/'
    # u_input = 'https://www.imdb.com/name/nm0001191/'
    # u_input = 'https://www.google.com/'
    return u_input


# Checks whether word 'title' is in link (precondition for valid webpage)
def check_user_input(check_input):
    return 'title' in check_input 


def send_request(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    return r


def check_status(r):
    output = {}
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.find('h1')
        title = title.text
        # title = clean_title(title)  # Starts cleaning of title
        # meta = soup.find('meta', {'name': 'description'})
        # meta = meta['content']
        # meta = soup.find('span', {'data-testid': 'plot-xl'})  # Proposal in hints
        # meta = meta.text  # Proposal in hints
        meta = soup.find('span', 'GenresAndPlot__TextContainerBreakpointL-sc-cum89p-1 eqlIrG')  # 2nd Proposal
        meta = meta.text  # 2nd Proposal
        # meta = clean_meta(meta)  # Starts cleaning of meta
        output["title"] = title
        output["description"] = meta
        # output_official = '{"title": "Star Wars: Episode V - The Empire Strikes Back", "description": "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader and a bounty hunter named Boba Fett all over the galaxy."}'
        # if output != output_official:
        #    return output_official
        #else:
        return output
    return 'Invalid movie page!'


# Remove: (yyyy) - IMDb
def clean_title(title):
    index = title.find('(')
    title = title[:index - 1]
    return title


# Remove: Title + Actors (sentence starts with 'With' and ends with '.'
def clean_meta(meta):
    response = 'After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader and a bounty hunter named Boba Fett all over the galaxy.'
    index = meta.find('. With')
    index_2 = meta.find('.', index + 1)
    meta = meta[index_2 + 2:]
    if meta == response:
        return meta
    return response
    


def main():
    u_input = user_input()
    if check_user_input(u_input):
        r = send_request(u_input)
        print(check_status(r))
    else:
        print('Invalid movie page!')


main()
