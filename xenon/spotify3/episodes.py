
# Import internal modules
from xenon.models import GetRequest, PutRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_EPISODE_IDS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, Episode

class GetEpisodes(GetRequest):
    """ Get Spotify catalog information for several episodes based on their Spotify IDs. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-multiple-episodes. """
    def __init__(self, episode_ids: list, market: str = current_users_market()) -> None:
        super().__init__()

        if len(episode_ids) > MAX_EPISODE_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned more than {MAX_EPISODE_IDS_COUNT} values.")
        if len(episode_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}"
        self.api_params = {
            'ids': config_list_to_comma_str(episode_ids),
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        episodes_list  = []
        for episode in self.get_data()['episodes']:
            episodes_list.append(Episode(episode))

        self._data = episodes_list

class GetCurrentUsersSavedEpisodes(GetRequest):
    """ Get a list of the episodes saved in the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-episodes.
    
    NOTE: This API endpoint is in beta and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). """
    def __init__(self, market: str = current_users_market(), limit: int = MAX_EPISODE_IDS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_EPISODE_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_EPISODE_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}"
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

class SaveEpisodesForCurrentUser(PutRequest):
    """ Save one or more episodes to the current user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-episodes-user. 
    
    NOTE: This API endpoint is in beta and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). """
    def __init__(self, episode_ids: list) -> None:
        super().__init__()

        if len(episode_ids) > MAX_EPISODE_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned more than {MAX_EPISODE_IDS_COUNT} values.")
        if len(episode_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}"
        self.api_params = {
            'ids': config_list_to_comma_str(episode_ids)
        }
        self.api_headers = _headers()

class RemoveCurrentUsersSavedEpisodes(DeleteRequest):
    """ Remove one or more episodes from the current user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-episodes-user.
    
    NOTE: This API endpoint is in beta and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). """
    def __init__(self, episode_ids: list) -> None:
        super().__init__()

        if len(episode_ids) > MAX_EPISODE_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned more than {MAX_EPISODE_IDS_COUNT} values.")
        if len(episode_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}"
        self.api_params = {
            'ids': config_list_to_comma_str(episode_ids)
        }
        self.api_headers = _headers()

class CheckUsersSavedEpisodes(GetRequest):
    """ Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-episodes.
    
    NOTE: This API endpoint is in beta and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). """
    def __init__(self,  episode_ids: list) -> None:
        super().__init__()

        if len(episode_ids) > MAX_EPISODE_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned more than {MAX_EPISODE_IDS_COUNT} values.")
        if len(episode_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'episode_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}"
        self.api_params = {
            'ids': config_list_to_comma_str(episode_ids)
        }
        self.api_headers = _headers()