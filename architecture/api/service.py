from utils.url import is_valid
from utils.url import short
from api.model import URL


class UrlDAO:
    host = ''

    def __init__(self):
        self.DB = {}

    def get_url_by_short(self, data, host):
        self.host = host

        shorted = data['shorted']
        for _, val in self.DB.items():
            if val.short == shorted:
                return val
        return None

    def _get_url_or_create(self, Url):
        for _, val in self.DB.items():
            if val.original == Url.original:
                return val

        return self._create(Url)

    def _create(self, Url):
        id = len(self.DB)
        Url.short = short(id, self.host)
        self.DB[id] = Url
        return Url

    def put(self, data, host):
        self.host = host

        Url = URL(original=data['url'])

        if not is_valid(Url.original):
            return None

        return self._get_url_or_create(Url)