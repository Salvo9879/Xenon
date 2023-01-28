
# Import internal modules
from xenon.models import GetRequest, PutRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_ALBUM_IDS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, Album

class GetAlbums(GetRequest):
    """ Get Spotify catalog information for multiple albums identified by their Spotify IDs. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-multiple-albums."""
    def __init__(self, album_ids: list, market: str = current_users_market()) -> None:
        super().__init__()

        if len(album_ids) > MAX_ALBUM_IDS_COUNT:
            raise ValueError(f"Parameter 'album_ids' returned more than {MAX_ALBUM_IDS_COUNT} values.")
        if len(album_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'album_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/albums"
        self.api_params = {
            'ids': config_list_to_comma_str(album_ids),
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        albums_list = []
        for album in self.get_data()['albums']:
            albums_list.append(Album(album))

        self._data = albums_list

class GetAlbumTracks(GetRequest):
    """ Get Spotify catalog information about an album's tracks. Optional parameters can be used to limit the number of tracks returned. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-albums-tracks. """
    def __init__(self, album_id: str, limit: int = MAX_ALBUM_IDS_COUNT, offset: int = 0, market: str = current_users_market()) -> None:
        super().__init__()

        if limit > MAX_ALBUM_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_ALBUM_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/albums/{album_id}/tracks"
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

class GetCurrentUsersSavedAlbums(GetRequest):
    """ Get a list of the albums saved in the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-albums. """
    def __init__(self, limit: int = MAX_ALBUM_IDS_COUNT, offset: int = 0, market: str = current_users_market()) -> None:
        super().__init__()

        if limit > MAX_ALBUM_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_ALBUM_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/albums"
        self.api_params = {
            'limit': limit,
            'offset': offset,
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to be returned to the caller. """
        self._data = FollowingRequest(self.get_data())

class SaveAlbumForCurrentUser(PutRequest):
    """ Save one or more albums to the current user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-albums-user. """
    def __init__(self, album_ids: list) -> None:
        super().__init__()

        if len(album_ids) > MAX_ALBUM_IDS_COUNT:
            raise ValueError(f"Parameter 'album_ids' returned more than {MAX_ALBUM_IDS_COUNT} values.")
        if len(album_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'album_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/albums"
        self.api_params = {
            'ids': config_list_to_comma_str(album_ids)
        }
        self.api_headers = _headers()

class RemoveCurrentUsersSavedAlbums(DeleteRequest):
    """ Remove one or more albums from the current user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-albums-user. """
    def __init__(self, album_ids: list) -> None:
        super().__init__()

        if len(album_ids) > MAX_ALBUM_IDS_COUNT:
            raise ValueError(f"Parameter 'album_ids' returned more than {MAX_ALBUM_IDS_COUNT} values.")
        if len(album_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'album_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/albums"
        self.api_params = {
            'ids': config_list_to_comma_str(album_ids)
        }
        self.api_headers = _headers()

class CheckCurrentUsersSavedAlbums(GetRequest):
    """ Check if one or more albums is already saved in the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-albums. """
    def __init__(self, album_ids: list) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/me/albums/contains"
        self.api_params = {
            'ids': config_list_to_comma_str(album_ids)
        }
        self.api_headers = _headers()

class GetNewReleases(GetRequest):
    """ Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player's “Browse” tab). https://developer.spotify.com/documentation/web-api/reference/#/operations/get-new-releases. """
    def __init__(self, market: str = current_users_market(), limit: int = MAX_ALBUM_IDS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_ALBUM_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_ALBUM_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/browse/new-releases"
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