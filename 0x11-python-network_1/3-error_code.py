#!/usr/bin/python3
"""sennds a req to URL to display body response"""
from urllib.request import Request, urlopen
from urllib.error import HTTPerror
from sys import argv


if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read()decode('utf-8'))
    except HTTPerror as status:
        print('Error code: {}'.format(status.code))
