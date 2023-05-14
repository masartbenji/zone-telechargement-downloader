import requests

from utils.HtmlUtils import HtmlUtils
from utils.AntiCaptcha import AntiCaptcha
from utils.DlProtect import DlProtect
from utils.hosts.OneFichierHost import OneFichierHost


class ZoneTelechargementLinkExtractor:

    def get_cookie(self, first_page_response):
        return first_page_response.cookies.get("PHPSESSID")

    def get_first_page_response(self, url):
        return requests.get(url)

    def get_dl_protect_link(self, url):
        response = self.get_first_page_response(url)
        html = HtmlUtils().parse(response.text)
        sitekey = html.find(class_="cf-turnstile").attrs.get("data-sitekey")
        cookie = self.get_cookie(response)
        token = AntiCaptcha().find_token(url, cookie, sitekey)
        if token:
            return DlProtect().get_protected_link(url, token)
        else:
            return

    def get_dl_protect_links(self, url):
        response = requests.get(url)
        html_response = HtmlUtils().parse(response.text)
        post_info = html_response.find(class_="postinfo")
        return OneFichierHost().get_links(post_info.findAll('b'))

    def find_links(self, url):
        dl_protect_links = self.get_dl_protect_links(url)
        protected_links = []
        for link in dl_protect_links:
            protected_link = self.get_dl_protect_link(link)
            if protected_link:
                protected_links.append(protected_link)
        return protected_links

    def find_multi_links(self, urls):
        for url in urls:
            self.find_links(url)
