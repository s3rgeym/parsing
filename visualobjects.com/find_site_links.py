#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup
BASE_URL = 'https://visualobjects.com/'
if len(sys.argv) == 1:
    print('Usage:', sys.argv[0], '<category eg web-development>')
    sys.exit()
category = sys.argv[1]
session = requests.session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
})
page = 1
while 1:
    r = session.get(f'{BASE_CATEGORY}/{category}', dict(page=page))
    s = BeautifulSoup(r.text)
    buttons = s.find_all('div', class_='details-website-button')
    for btn in buttons:
        print(btn.find('a')['href'], flush=True)
    if len(buttons) < page_size:
        break
    page += 1
