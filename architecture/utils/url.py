from urllib.parse import urlparse
from urllib.parse import urljoin
import string
import random
from math import floor


def is_valid(s):
    parsed_url = urlparse(s)
    return bool(parsed_url.scheme)

def short(id, host):
    n = floor(id%3 + random.randint(3, 5))
    tail = ''.join(
        random.choice(
            string.ascii_letters + string.digits
            ) for _ in range(n))

    return urljoin(host, tail)