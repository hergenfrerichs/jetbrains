import requests

def user_input():
    u_input = input()
    # u_input = 'https://www.facebook.com/'
    # u_input = 'http://google.com/asdfg'
    return u_input


def send_request(url):
    r = requests.get(url)
    return r


def save_content(r):
    my_file = open('source.html', 'wb')
    my_file.write(r.content)
    my_file.close()


def main():
    u_input = user_input()
    r = send_request(u_input)
    if r:
        save_content(r)
        print('Content saved.')
    else:
        print(f'The URL returned {r.status_code}!')


main()
