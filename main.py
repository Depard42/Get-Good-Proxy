'''
Proxy catcher from https://free-proxy-list.net/
Maid by Depard42
'''

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json

url = "https://free-proxy-list.net/"
SAVE_NAME = 'proxy.json'


headers = {
    "authority": "free-proxy-list.net",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru,en;q=0.9",
    "cache-control": "max-age=0",
    "if-modified-since": "Sun, 10 Dec 2023 17:32:02 GMT",
    "sec-ch-ua": '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.732 YaBrowser/23.11.1.732 Yowser/2.5 Safari/537.36"
}


def get_proxy() -> list:
    '''
    return list of dicts with attrs:
    ip, port, code, country, anonimity, google, https, checked
    '''
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url)
    if not response:
        return None
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('div', {'class': "table-responsive fpl-list"})
    if not table:
        return None
    proxy = []
    for tr in table.find_all('tr')[1:]:
        ip, port, code, country, anonimity, google, https, checked = list(map(lambda el: el.text.strip(), tr.find_all('td')))
        proxy.append({
            'ip': ip,
            'port': port,
            'code': code,
            'country': country,
            'anonimity': anonimity,
            'google': google,
            'https': https,
            'checked': checked
        })
    return proxy



def main():
    proxy = get_proxy()
    if proxy:
        dir = Path(__file__).parent.joinpath(SAVE_NAME)
        with open(dir, 'w', encoding='utf-8') as file:
            json.dump(proxy, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()