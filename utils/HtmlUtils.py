from bs4 import BeautifulSoup


class HtmlUtils:
    def parse(self, html_text):
        return BeautifulSoup(html_text, "html.parser")