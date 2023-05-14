from utils.hosts.FileHost import FileHost


class NitroFlareHost(FileHost):
    def get_name(self):
        return "Nitroflare"

    def is_favorite(self):
        return False