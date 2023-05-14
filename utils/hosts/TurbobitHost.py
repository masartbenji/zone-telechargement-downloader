from utils.hosts.FileHost import FileHost


class TurbobitHost(FileHost):
    def get_name(self):
        return "Turbobit"

    def is_favorite(self):
        return False