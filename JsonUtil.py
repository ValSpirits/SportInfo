import urllib.request


class JsonUtil:
    @classmethod
    def http_get(cls,url):
        response  = urllib.request.urlopen(url)
        return response.read().decode('unicode_escape')
