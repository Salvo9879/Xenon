
# Import external modules
from flask import Flask

# Import internal modules
from .config import ServerSettings
from .databases import db

class Xenon():
    def __init__(server, import_name: str) -> None:
        server.app = Flask(import_name)
        server.ss = ServerSettings()
        server.db = db.init_app()
        
    def run(server):
        server.app.run(
            host = server.ss.host,
            port = server.ss.port,
            debug = server.ss.debug
        )