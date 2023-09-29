#!/usr/bin/python3
"""Fetches https://alx-intranet.htbn.io/status."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.htbn.io/status")
    with urllib.request.urlopen(request) as reqponse:
        body = reqponse.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
