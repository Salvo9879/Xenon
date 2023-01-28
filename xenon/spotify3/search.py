
# Import internal modules
from xenon.models import GetRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_PLAYLIST_ITEMS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import SearchResults

class SearchForItem(GetRequest):
    """ Get Spotify catalog information about albums, artists, playlists, tracks, shows, episodes or audiobooks that match a keyword string.
    
    NOTE: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets. """
    def __init__(self, search_query: str, filters: list = ['album', 'artist', 'playlist', 'track', 'show', 'episode', 'audiobook'], limit: int = MAX_PLAYLIST_ITEMS_COUNT, offset: int = 0, market: str = current_users_market()) -> None:
        super().__init__()

        if limit > MAX_PLAYLIST_ITEMS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_PLAYLIST_ITEMS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/search"
        self.api_params = {
            'q': search_query,
            'type': config_list_to_comma_str(filters),
            'limit': limit,
            'offset': offset,
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = SearchResults(self.get_data())