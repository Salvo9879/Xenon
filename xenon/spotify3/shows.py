
# Import internal modules
from xenon.models import GetRequest, PutRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_SHOW_IDS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, Show

class GetShows(GetRequest):
    """ Get Spotify catalog information for several artists based on their Spotify IDs. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-multiple-artists. """
    def __init__(self, show_ids: list) -> None:
        super().__init__()

        if len(show_ids) > MAX_SHOW_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned more than {MAX_SHOW_IDS_COUNT} values.")
        if len(show_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/shows"
        self.api_params = {
            'ids': config_list_to_comma_str(show_ids)
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        shows_list = []
        for show in self.get_data()['shows']:
            shows_list.append(Show(show))
        
        self._data = shows_list


class GetShowEpisodes(GetRequest):
    """ Get Spotify catalog information about an show's episodes. Optional parameters can be used to limit the number of episodes returned. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-a-shows-episodes. """
    def __init__(self, show_id: str, market: str = current_users_market(), limit: int = MAX_SHOW_IDS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_SHOW_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_SHOW_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/shows/{show_id}/episodes"
        self.api_params = {
            'market': market,
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())


class GetCurrentUsersSavedShows(GetRequest):
    """ Get a list of shows saved in the current Spotify user's library. Optional parameters can be used to limit the number of shows returned. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-shows. """
    def __init__(self, limit: int = MAX_SHOW_IDS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_SHOW_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_SHOW_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/shows"
        self.api_params = {
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        self._data = FollowingRequest(self.get_data())

class SaveShowsForCurrentUser(PutRequest):
    """ Save one or more shows to current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-shows-user. """
    def __init__(self, show_ids: list) -> None:
        super().__init__()

        if len(show_ids) > MAX_SHOW_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned more than {MAX_SHOW_IDS_COUNT} values.")
        if len(show_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/shows"
        self.api_params = {
            'ids': config_list_to_comma_str(show_ids)
        }
        self.api_headers = _headers()

class RemoveCurrentUsersSavedShows(DeleteRequest):
    """ Delete one or more shows from current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-shows-user. """
    def __init__(self, show_ids: list, market: str = current_users_market()) -> None:
        super().__init__()

        if len(show_ids) > MAX_SHOW_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned more than {MAX_SHOW_IDS_COUNT} values.")
        if len(show_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/shows"
        self.api_params = {
            'ids': config_list_to_comma_str(show_ids),
            'market': market
        }
        self.api_headers = _headers()

class CheckCurrentUsersSavedShow(GetRequest):
    """ Check if one or more shows is already saved in the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-shows. """
    def __init__(self, show_ids: list) -> None:
        super().__init__()

        if len(show_ids) > MAX_SHOW_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned more than {MAX_SHOW_IDS_COUNT} values.")
        if len(show_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'show_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/shows/contains"
        self.api_params = {
            'ids': config_list_to_comma_str(show_ids)
        }
        self.api_headers = _headers()