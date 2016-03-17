#!/usr/bin/env python3

### Validate URLs found in markdown documents using HEAD requests

import sys, markdown, requests, bs4 as BeautifulSoup

def check_url(url):
    try:
        return bool(requests.head(url, allow_redirects=True))
    except Exception as e:
        print ('Error checking URL %s: %s' % (url, e))
        return False

def retrieve_urls(filename):
    with open(filename) as fd:
        mdtext = fd.read()
        html_text = markdown.markdown(mdtext)
        soup = BeautifulSoup.BeautifulSoup(html_text)
        return [a['href'] for a in soup.findAll('a')]

def check_urls(filename):
    print ('checking URLs for %s' % (filename,))
    ok = True
    for url in retrieve_urls(filename):
        msg = 'Checking %s => ' % (url,)
        if check_url(url):
            print (msg + 'OK')
        else:
            print (msg + 'FAILED')
            ok = False
    return ok

def main():
    ok = True
    for filename in sys.argv[1:]:
        try:
            ok &= check_urls(filename)
        except IOError as e:
            print (e)
            ok = False
    exit (0 if ok else 1)

if __name__ == '__main__':
    main()
