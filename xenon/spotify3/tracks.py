
# Import internal modules
from xenon.models import GetRequest, PutRequest, DeleteRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_TRACK_IDS_COUNT, MIN_IDS_COUNT, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import FollowingRequest, Track, AudioFeatures

class GetTracks(GetRequest):
    """ Get Spotify catalog information for multiple tracks based on their Spotify IDs. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-tracks. """
    def __init__(self, track_ids: list, market: str = current_users_market()) -> None:
        super().__init__()

        if len(track_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(track_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/tracks"
        self.api_params = {
            'ids': config_list_to_comma_str(track_ids),
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

class GetCurrentUsersSavedTracks(GetRequest):
    """ Get a list of the songs saved in the current Spotify user's 'Your Music' library. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-tracks. """
    def __init__(self, limit: int = MAX_TRACK_IDS_COUNT, offset: int = 0, market: str = current_users_market()) -> None:
        super().__init__()

        if limit > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if limit < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'limit' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/tracks"
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

class SaveTracksForCurrentUser(PutRequest):
    """ Save one or more tracks to the current user's 'Your Music' library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-tracks-user. """
    def __init__(self, track_ids: list) -> None:
        super().__init__()

        if len(track_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(track_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/tracks"
        self.api_params = {
            'ids': config_list_to_comma_str(track_ids)
        }
        self.api_headers = _headers()

class RemoveUsersSavedTrack(DeleteRequest):
    """ Remove one or more tracks from the current user's 'Your Music' library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-tracks-user. """
    def __init__(self, track_ids: list) -> None:
        super().__init__()

        if len(track_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(track_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/tracks"
        self.api_params = {
            'ids': config_list_to_comma_str(track_ids)
        }
        self.api_headers = _headers()

class CheckUsersSavedTracks(GetRequest):
    """ Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-tracks. """
    def __init__(self, track_ids: list) -> None:
        super().__init__()

        if len(track_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(track_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/me/tracks/contains"
        self.api_params = {
            'ids': config_list_to_comma_str(track_ids)
        }
        self.api_headers = _headers()

class GetTracksAudioFeatures(GetRequest):
    """ Get audio features for multiple tracks based on their Spotify IDs. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features. """
    def __init__(self, track_ids: list) -> None:
        super().__init__()

        if len(track_ids) > MAX_TRACK_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned more than {MAX_TRACK_IDS_COUNT} values.")
        if len(track_ids) < MIN_IDS_COUNT:
            raise ValueError(f"Parameter 'track_ids' returned less than {MIN_IDS_COUNT} values.")

        self.api_url = f"{BASE_URL}/audio-features"
        self.api_params = {
            'ids': config_list_to_comma_str(track_ids)
        }
        self.api_headers = _headers()

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = AudioFeatures(self.get_data())

class GetTrackAudioAnalysis(GetRequest):
    """ Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track's structure and musical content, including rhythm, pitch, and timbre. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-analysis 
    
    TODO: Create the functions
    """
    def __init__(self) -> None:
        super().__init__()
        raise AttributeError('THIS FUNCTION IS CURRENTLY NOT AVAILABLE.')

class GetRecommendations(GetRequest):
    """ Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations.

    For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks. 
    
    TODO: Review this whole function - more specifically how the api works. As of now it only takes in required parameters, however there are many more to include.
    """
    def __init__(self, seed_genres: str, seed_tracks: str, limit: int = MAX_TRACK_IDS_COUNT, offset: int = 0) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/recommendations"
        self.api_params = {
            'limit': limit,
            'offset': offset,
            'seed_genres': seed_genres,
            'seed_tracks': seed_tracks
        }
        self.api_headers = _headers()

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        # TODO: Create code which also returns the seed recommendation objects

        tracks_list = []
        for track in self.get_data()['track']:
            tracks_list.append(Track(track))

        self._data = tracks_list