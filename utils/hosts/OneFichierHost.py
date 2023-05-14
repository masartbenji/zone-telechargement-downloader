from utils.hosts.FileHost import FileHost


class OneFichierHost(FileHost):
    def is_favorite(self):
        return True

    def get_name(self):
        return "1fichier"
