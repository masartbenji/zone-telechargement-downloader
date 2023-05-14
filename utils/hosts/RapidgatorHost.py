from utils.hosts.FileHost import FileHost


class RapidgatorHost(FileHost):
    def get_name(self):
        return "Rapidgator"

    def is_favorite(self):
        return False