import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import unquote
from support.config import get_item


logger = logging.getLogger(__name__)


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,\
    image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;\
    v=b3;q=0.7",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"'
}

_charsets = ['GB', 'UTF', 'ISO']


def fetch(url, type='soup'):
    url = unquote(url)
    proxy_url = get_item('PROXY_URL')
    try:
        logger.debug(f'fetch url: {url}')
        response = requests.get(url, headers=headers, timeout=30000)
        if response.status_code > 300:
            raise RuntimeError(f'status err : {response.status_code},\
                                err: {response.content}')
        # print(response.apparent_encoding)
        ec = response.apparent_encoding
        if ec and len(list(filter(lambda c: c in ec, _charsets))):
            response.encoding = response.apparent_encoding
        else:
            response.encoding = 'utf-8'
        if type == 'soup':
            return BeautifulSoup(response.text, 'html.parser')
        elif type == 'text':
            return response.text
        else:
            return response
    except requests.exceptions.ConnectionError as conection_e:
        err = conection_e
    except requests.exceptions.HTTPError as http_err:
        err = http_err
    except Exception as e:
        err = e
    if proxy_url not in url:
        return fetch(proxy_url+"?url="+url, type)
    else:
        logger.warning(f"error: {err}")
        raise err
