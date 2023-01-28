
# Import internal modules
from xenon.models import GetRequest, PutRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_ARTIST_IDS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, Artist, Track

class GetArtists(GetRequest):
    """ Get Spotify catalog information for several artists based on their Spotify IDs. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-multiple-artists. """
    def __init__(self, artist_ids: list) -> None:
        super().__init__()

        if len(artist_ids) > MAX_ARTIST_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned more than {MAX_ARTIST_IDS_COUNT} values.")
        if len(artist_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/artists"
        self.api_params = {
            'ids': artist_ids
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        artists_list = []
        for artist in self.get_data()['artists']:
            artists_list.append(Artist(artist))
        
        self._data = artists_list

class GetArtistsAlbums(GetRequest):
    """ Get Spotify catalog information about an artist's albums. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-albums. """
    def __init__(self, artist_id: str, include_groups: list = ['album', 'single', 'appears_on', 'compilation'], limit: int = MAX_ARTIST_IDS_COUNT, offset: int = 0, market: str = current_users_market()) -> None:
        super().__init__()

        if limit > MAX_ARTIST_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_ARTIST_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/artists/{artist_id}/albums"
        self.api_params = {
            'include_groups': include_groups,
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetArtistsTopTracks(GetRequest):
    """ Get Spotify catalog information about an artist's top tracks by country. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-top-tracks. """
    def __init__(self, artist_id: str, market: str = current_users_market()) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/artists/{artist_id}/top-tracks"
        self.api_params = {
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        tracks_list = []
        for track in self.get_data()['tracks']:
            tracks_list.append(Track(track))

        self._data = tracks_list

class GetArtistsRelatedArtists(GetRequest):
    """ Get Spotify catalog information about artists similar to a given artist. Similarity is based on analysis of the Spotify community's listening history. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-related-artists. """
    def __init__(self, artist_id: str) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/artists{artist_id}/related-artists"
        self.api_params = {
            'id': artist_id
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        artists_list = []
        for artist in self.get_data()['artists']:
            artists_list.append(Artist(artist))
        
        self._data = artists_list

class FollowArtist(PutRequest):
    """ Add the current user as a follower of one or more artists. https://developer.spotify.com/documentation/web-api/reference/#/operations/follow-artists-users. """
    def __init__(self, artist_ids: list) -> None:
        super().__init__()

        if len(artist_ids) > MAX_ARTIST_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned more than {MAX_ARTIST_IDS_COUNT} values.")
        if len(artist_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/following"
        self.api_params = {
            'type': 'artist',
            'ids': config_list_to_comma_str(artist_ids)
        }
        self.api_headers = _headers()

class UnfollowArtist(DeleteRequest):
    """ Remove the current user as a follower of one or more artists. https://developer.spotify.com/documentation/web-api/reference/#/operations/unfollow-artists-users """
    def __init__(self, artist_ids: list) -> None:
        super().__init__()

        if len(artist_ids) > MAX_ARTIST_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned more than {MAX_ARTIST_IDS_COUNT} values.")
        if len(artist_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/following"
        self.api_params = {
            'type': 'artist',
            'ids': config_list_to_comma_str(artist_ids)
        }
        self.api_headers = _headers()

class CheckIfUserFollowsArtists(GetRequest):
    """ Check to see if the current user is following one or more artists. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-current-user-follows. """
    def __init__(self, artist_ids: list) -> None:
        super().__init__()

        if len(artist_ids) > MAX_ARTIST_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned more than {MAX_ARTIST_IDS_COUNT} values.")
        if len(artist_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'artist_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/following/contains"
        self.api_params = {
            'type': 'artist',
            'ids': config_list_to_comma_str(artist_ids)
        }
        self.api_headers = _headers()