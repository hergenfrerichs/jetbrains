import requests

def user_input():
    u_input = input()
    # u_input = 'http://api.quotable.io/authors'
    # u_input = 'http://api.quotable.io/authors'
    # u_input = 'http://api.quotable.io/quotes/1'
    # u_input = 'http://api.quotable.io/quotes/-CzNrWMGIg8V'
    return u_input


def send_request(url):
    r = requests.get(url)
    return r


def check_status(r):
    if r:
        r_json = r.json()
        try:
            return r_json['content']
        except KeyError:
            return 'Invalid quote resource!'
    return 'Invalid quote resource!'
    


def main():
    u_input = user_input()
    r = send_request(u_input)
    print(check_status(r))


main()


