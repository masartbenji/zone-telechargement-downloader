from abc import ABC, abstractmethod

from bs4 import ResultSet


class FileHost(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def is_favorite(self):
        pass

    def get_links(self, post_info_children: ResultSet):
        already_set = False
        links = []

        for tag in post_info_children:
            if tag.findNext().name == 'div':
                if tag.text.__contains__(self.get_name()):
                    already_set = True
                elif already_set:
                    break
            elif tag.findNext().name == 'a' and already_set:
                links.append(tag.findNext().attrs.get("href"))
        return links