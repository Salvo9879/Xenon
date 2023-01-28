
# Import internal modules
from xenon.models import GetRequest, PutRequest, PostRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_PLAYLIST_ITEMS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, Playlist

class GetPlaylist(GetRequest):
    """ Get a playlist owned by a Spotify user. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlist. """
    def __init__(self, playlist_id: str, market: str = current_users_market()) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}"
        self.api_params = {
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = Playlist(self.get_data())

class ChangePlaylistDetails(PutRequest):
    """ Change a playlist's name and public/private state. (The user must, of course, own the playlist). https://developer.spotify.com/documentation/web-api/reference/#/operations/change-playlist-details. """
    def __init__(self, playlist_id: str, name: str = None, is_public: bool = None, is_collaborative: bool = None, description: str = None) -> None:
        super().__init__()

        if name is not None:
            self.api_payload.update({'name': name})
        if is_public is not None:
            self.api_payload.update({'public': is_public})
        if is_collaborative is not None:
            self.api_payload.update({'collaborative': is_collaborative})
        if description is not None:
            self.api_payload.update({'description': description})

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}"
        self.api_params = {}
        self.api_headers = _headers()

class GetPlaylistItems(GetRequest):
    """ Get full details of the items of a playlist owned by a Spotify user. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlists-tracks. """
    def __init__(self, playlist_id: str, limit: int = MAX_PLAYLIST_ITEMS_COUNT, offset: int = 0, market: str = current_users_market()) -> None:
        super().__init__()

        if limit > MAX_PLAYLIST_ITEMS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_PLAYLIST_ITEMS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}/tracks"
        self.api_params = {
            'limit': limit,
            'offset': offset,
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class AddItemsToPlaylist(PostRequest):
    """ Add one or more items to a user's playlist. https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist. """
    def __init__(self, playlist_id: str, item_uris: list, position: int = None) -> None:
        super().__init__()

        if position is not None:
            self.api_params.update({'position': position})

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}"
        self.api_params = {
            'uris': config_list_to_comma_str(item_uris)
        }
        self.api_headers = _headers()

class ReorderPlaylistItems(PutRequest):
    """ Reorders items in a playlist. https://developer.spotify.com/documentation/web-api/reference/#/operations/reorder-or-replace-playlists-tracks. """
    def __init__(self, playlist_id: str, range_start: int, range_length: int, insert_before: int) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}/tracks"
        self.api_params = {
            'range_start': range_start,
            'range_length': range_length,
            'insert_before': insert_before
        }
        self.api_headers = _headers()

class RemovePlaylistItems(DeleteRequest):
    """ Remove one or more items from a user's playlist. """
    def __init__(self, playlist_id: str, track_uris: list) -> None:
        super().__init__()

        tracks = []
        for track in track_uris:
            tracks.append({'uri': track})

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}/tracks"
        self.api_params = {}
        self.api_headers = _headers()
        self.api_payload = {
            'tracks': tracks
        }

class GetCurrentUsersPlaylists(GetRequest):
    """ Get a list of the playlists owned or followed by the current Spotify user. """
    def __init__(self, limit: int = MAX_PLAYLIST_ITEMS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_PLAYLIST_ITEMS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_PLAYLIST_ITEMS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/playlists"
        self.api_params = {
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetUsersPlaylists(GetRequest):
    """ Get a list of the playlists owned or followed by a Spotify user. """
    def __init__(self, user_id: str, limit: int = MAX_PLAYLIST_ITEMS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_PLAYLIST_ITEMS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_PLAYLIST_ITEMS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/users/{user_id}/playlists"
        self.api_params = {
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()
        
        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class CreatePlaylist(PostRequest):
    """ Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist).) """
    def __init__(self, user_id: str, name: str, is_public: bool = False, is_collaborative: bool = False, description: str = '') -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/users/{user_id}/playlists"
        self.api_params = {}
        self.api_headers = _headers()
        self.api_payload = {
            'name': name,
            'public': is_public,
            'collaborative': is_collaborative,
            'description': description
        }

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = Playlist(self.get_data())

class GetFeaturedPlaylists(GetRequest):
    """ Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab). """
    def __init__(self, limit: int = MAX_PLAYLIST_ITEMS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_PLAYLIST_ITEMS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_PLAYLIST_ITEMS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/browse/featured-playlists"
        self.api_params = {
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetCategoryPlaylists(GetRequest):
    """ Get a list of Spotify playlists tagged with a particular category. """
    def __init__(self, category_id: str, market: str = current_users_market(), limit: int = MAX_PLAYLIST_ITEMS_COUNT, offset: int = 0) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/browse/categories/{category_id}/playlists"
        self.api_params = {
            'country': market,
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetPlaylistCoverImage(GetRequest):
    """ Get the current image associated with a specific playlist. """
    def __init__(self, playlist_id: str) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}/images"
        self.api_params = {}
        self.api_headers = _headers()

class AddCustomPlaylist(PutRequest):
    """ Replace the image used to represent a specific playlist. """
    def __init__(self, playlist_id: str) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/playlists/{playlist_id}/images"
        self.api_params = {}
        self.api_headers = _headers()
