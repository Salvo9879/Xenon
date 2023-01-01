
# Import external modules
from configparser import ConfigParser

class ServerSettings():
    def __init__(self, fp='config.ini') -> None:
        cp = ConfigParser()
        cp.read(f"instance/{fp}")
        self.cp = cp['SERVER']

        self.configure_settings()

    def configure_settings(self):
        for item, value in self.cp.items():
            setattr(self, item, value)