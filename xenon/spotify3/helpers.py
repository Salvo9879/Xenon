
# Import external modules
from flask_login import current_user

BASE_URL = 'https://api.spotify.com/v1'

MAX_ALBUM_IDS_COUNT = 20
MAX_ARTIST_IDS_COUNT = 50
MAX_SHOW_IDS_COUNT = 50
MAX_EPISODE_IDS_COUNT = 50
MAX_AUDIOBOOK_IDS_COUNT = 50
MAX_TRACK_IDS_COUNT = 50
MAX_PLAYLIST_ITEMS_COUNT = 50 #? This may need to be revised
MAX_PLAYER_ITEMS_COUNT = 50

MIN_IDS_COUNT = 1

_TOKEN = ''

def current_users_market() -> str:
    """ Gets the ISO 3166-1 alpha-2 country code of the user """
    return 'gb'
    # return current_user.spotify_country_code

def _headers() -> dict:
    return {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {_TOKEN}"
    }

def config_list_to_comma_str(data_list: list) -> str:
    """ Converts a Python list into a comma-separated string. """
    return ','.join(data_list)