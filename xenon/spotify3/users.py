
# Import internal modules
from xenon.models import GetRequest, PutRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_TRACK_IDS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, User

# PLAYLISTS
# Follow playlist
# Unfollow playlist
# Check if user follows playlist

class GetCurrentUsersProfile(GetRequest):
    """ Get detailed profile information about the current user (including the current user's username). https://developer.spotify.com/documentation/web-api/reference/#/operations/get-current-users-profile. """
    def __init__(self) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/me"
        self.api_params = {}
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = User(self.get_data())

class GetCurrentUsersTopItems(GetRequest):
    """ Get the current user's top artists or tracks based on calculated affinity. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-top-artists-and-tracks. """
    def __init__(self, limit: int = MAX_TRACK_IDS_COUNT, offset: int = 0, time_range: str = 'medium_term') -> None:
        super().__init__()

        if limit > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/top/type"
        self.api_params = {
            'limit': limit,
            'offset': offset,
            'time_range': time_range
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetUsersProfile(GetRequest):
    """ Get public profile information about a Spotify user. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-profile. """
    def __init__(self, user_id: str) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/users/{user_id}"
        self.api_params = {}
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetCurrentUsersFollowedArtists(GetRequest):
    """ Get the current user's followed artists. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-followed. """
    def __init__(self, after: str = None, limit: int = MAX_TRACK_IDS_COUNT) -> None:
        super().__init__()

        if after is not None:
           self.api_params.values({'after': after}) 

        self.api_url = f"{BASE_URL}/me/following"
        self.api_params = {
            'limit': limit
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class FollowUser(PutRequest):
    """ Add the current user as a follower of one or more Spotify users. https://developer.spotify.com/documentation/web-api/reference/#/operations/follow-artists-users. """
    def __init__(self, user_ids: list) -> None:
        super().__init__()

        if len(user_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'user_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(user_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'user_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/following"
        self.api_params = {
            'type': 'user',
            'ids': config_list_to_comma_str(user_ids)
        }
        self.api_headers = _headers()

class UnfollowUser(DeleteRequest):
    """ Remove the current user as a follower of one or more Spotify users. https://developer.spotify.com/documentation/web-api/reference/#/operations/unfollow-artists-users. """
    def __init__(self, user_ids: list) -> None:
        super().__init__()

        if len(user_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'user_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(user_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'user_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/following"
        self.api_params = {
            'type': 'user',
            'ids': config_list_to_comma_str(user_ids)
        }
        self.api_headers = _headers()

class CheckIfUserFollowsUser(GetRequest):
    """ Check to see if the current user is following one or more Spotify users. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-current-user-follows.  """
    def __init__(self, user_ids: list) -> None:
        super().__init__()

        if len(user_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'user_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(user_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'user_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/following/contains"
        self.api_params = {
            'type': 'user',
            'ids': user_ids
        }
        self.api_headers = _headers()
