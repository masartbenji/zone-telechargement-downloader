from utils.hosts.FileHost import FileHost


class UptoboxHost(FileHost):
    def get_name(self):
        return "Uptobox"

    def is_favorite(self):
        return False
