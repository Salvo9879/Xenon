from flask import Flask, redirect, request, url_for
from base64 import b64encode
from requests import post
import json

app = Flask(__name__)

AUTH = '' # Add authorization code

@app.route('/authorization')
def authorization():
    # http://localhost:5000
    scopes = 'ugc-image-upload,user-read-playback-state,app-remote-control,user-modify-playback-state,playlist-read-private,user-follow-modify,playlist-read-collaborative,user-follow-read,user-read-currently-playing,user-read-playback-position,user-library-modify,playlist-modify-private,playlist-modify-public,user-read-email,user-top-read,streaming,user-read-recently-played,user-read-private,user-library-read'
    return redirect(f"https://accounts.spotify.com/authorize?client_id=c3df48e3ffb2465e9eba67f69ff93f98&response_type=code&redirect_uri=http://localhost:5000/access_confirmed&state=ce71e51973689aa0c27f4a36b824db4ef642aaef8b1892c7f62601b8f49acaf0&scope={scopes}&show_dialog=true")

@app.route('/access_confirmed')
def access_confirmed():
    payload = f"grant_type=authorization_code&code={request.args.get('code')}&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Faccess_confirmed"
    headers = {
        'Authorization': f"Basic {AUTH}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    r = post('https://accounts.spotify.com/api/token', data=payload, headers=headers).json()

    with open('instance/spt.json', 'r') as f:
        data = json.load(f)


    data['access_token'] = r['access_token']
    data['refresh_token'] = r['refresh_token']

    with open('instance/spt.json', 'w') as f:
        json.dump(data, f, indent=4)

    return redirect(url_for('index'))

@app.route('/refresh')
def refresh():
    with open('instance/spt.json', 'r') as f:
        data = json.load(f)

    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': data['refresh_token']
    }
    headers = {
        'Authorization': f"Basic {AUTH}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    r = post('https://accounts.spotify.com/api/token', data=payload, headers=headers).json()

    return redirect(url_for('index'))


@app.route('/')
def index():
    # http://localhost:5000
    with open('instance/spt.json', 'r') as f:
        data = json.load(f)

    return f"<p><a href=\"http://localhost:5000/authorization\">Authorize</a> <a href=\"http://localhost:5000/refresh\">Refresh</a></p><p><b>ACCESS TOKEN:</b> {data['access_token']}</p><p><b>REFRESH TOKEN:</b> {data['refresh_token']}</p>"

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000,
        host='0.0.0.0'
    )