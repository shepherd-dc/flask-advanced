import requests


class HTTP:
    @staticmethod
    def get(url, request_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if request_json else ''
        return r.json() if request_json else r.text
