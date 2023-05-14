import requests

from utils.HtmlUtils import HtmlUtils


class DlProtect:
    def get_protected_link(self, url, token):
        json_object = {'subform': 'unlock', 'cf-turnstile-response': token}
        response = requests.post(url, data=json_object)
        html = HtmlUtils().parse(response.text)
        urls = html.find(class_="urls")
        return urls.find("a").attrs.get("href")
