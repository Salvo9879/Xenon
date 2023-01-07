
# Import external modules
from configparser import ConfigParser

class ServerSettings():
    """ Object which gets all the settings needed for the server to work. It gets these settings from a `.ini` file. The fp of the file is taken in as an argument by parameter `fp`. """

    def __init__(self, fp: str ='config.ini') -> None:
        cp = ConfigParser()
        cp.read(f"instance/{fp}")
        self.cp = cp['SERVER']

        self.configure_settings()

    def configure_settings(self) -> None:
        """ Makes any settings recovered by the config file into an object attribute. """

        for item, value in self.cp.items():
            setattr(self, item, value)