#!/usr/bin/python3
"""fetch the status of https://alx-intranet.hbnb.io/status"""


if __name__ == "__main__":
    import urllib.request

    '''url http service'''
    url = 'https://intranet.hbnb.io/status'

    with request.urlopen(url) as response:
        html_body = response.read()
        print('Body response:')
        print('\t- typr: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
