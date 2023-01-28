
# Import internal modules
from xenon.models import GetRequest, PutRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_AUDIOBOOK_IDS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, Audiobook

class GetAudiobooks(GetRequest):
    """ Get Spotify catalog information for several audiobooks identified by their Spotify IDs. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-multiple-audiobooks.

    NOTE: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets. """
    def __init__(self, audiobook_ids: list, market: str = current_users_market()) -> None:
        super().__init__()

        if len(audiobook_ids) > MAX_AUDIOBOOK_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned more than {MAX_AUDIOBOOK_IDS_COUNT} values.")
        if len(audiobook_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned less than {MIN_IDS_COUNT} values.") 

        self.api_url = f"{BASE_URL}/audiobooks"
        self.api_params = {
            'ids': config_list_to_comma_str(audiobook_ids),
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        audiobooks_list = []
        for audiobook in self.get_data()['audiobooks']:
            audiobooks_list.append(Audiobook(audiobook))

        self._data = audiobooks_list

class GetAudiobookChapter(GetRequest):
    """ Get Spotify catalog information about an audiobook's chapters. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audiobook-chapters.

    NOTE: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets. """
    def __init__(self, audiobook_id: str, limit: int = MAX_AUDIOBOOK_IDS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_AUDIOBOOK_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_AUDIOBOOK_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/audiobooks/{audiobook_id}/chapters"
        self.api_params = {
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True
    
    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetCurrentUsersSavedAudiobooks(GetRequest):
    """ Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-audiobooks. """
    def __init__(self, limit: int = MAX_AUDIOBOOK_IDS_COUNT, offset: int = 0) -> None:
        super().__init__()

        if limit > MAX_AUDIOBOOK_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_AUDIOBOOK_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/audiobooks"
        self.api_params = {
            'limit': limit,
            'offset': offset
        }
        self.api_headers = _headers()

        self.cdq = True
    
    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())


class SaveAudiobookForCurrentUser(PutRequest):
    """ Save one or more audiobooks to the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-audiobooks-user. """
    def __init__(self, audiobook_ids: list) -> None:
        super().__init__()

        if len(audiobook_ids) > MAX_AUDIOBOOK_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned more than {MAX_AUDIOBOOK_IDS_COUNT} values.")
        if len(audiobook_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned less than {MIN_IDS_COUNT} values.") 

        self.api_url = f"{BASE_URL}/me/audiobooks"
        self.api_params = {
            'ids': config_list_to_comma_str(audiobook_ids)
        }
        self.api_headers = _headers()

class RemoveUsersSavedAudiobooks(DeleteRequest):
    """ Remove one or more audiobooks from the Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-audiobooks-user. """
    def __init__(self, audiobook_ids: list) -> None:
        super().__init__()

        if len(audiobook_ids) > MAX_AUDIOBOOK_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned more than {MAX_AUDIOBOOK_IDS_COUNT} values.")
        if len(audiobook_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned less than {MIN_IDS_COUNT} values.") 

        self.api_url = f"{BASE_URL}/me/audiobooks"
        self.api_params = {
            'ids': config_list_to_comma_str(audiobook_ids)
        }
        self.api_headers = _headers()

class CheckUsersSavedAudiobooks(GetRequest):
    """ Check if one or more audiobooks are already saved in the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-audiobooks. """
    def __init__(self, audiobook_ids: list) -> None:
        super().__init__()

        if len(audiobook_ids) > MAX_AUDIOBOOK_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned more than {MAX_AUDIOBOOK_IDS_COUNT} values.")
        if len(audiobook_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'audiobook_ids' returned less than {MIN_IDS_COUNT} values.") 

        self.api_url = f"{BASE_URL}/me/audiobooks/contains"
        self.api_params = {
            'ids': config_list_to_comma_str(audiobook_ids)
        }
        self.api_headers = _headers()