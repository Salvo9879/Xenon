
# Import internal modules
from xenon import db, ServerSettings

# Import external modules
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///users.db',
    'apis': 'sqlite:///apis.db',
    'govee': 'sqlite:///govee.db'
}

ss = ServerSettings()
db.init_app(app)

if __name__ == '__main__':
    app.run(
        host=ss.host,
        port=ss.port,
        debug=ss.debug
    )