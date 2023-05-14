from utils.hosts.FileHost import FileHost


class FilericeHost(FileHost):
    def get_name(self):
        return "Filerice"

    def is_favorite(self):
        return False