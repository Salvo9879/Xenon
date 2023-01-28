
# Import internal modules
from xenon.models import GetRequest, PutRequest, PostRequest
from xenon.spotify3.helpers import _headers, BASE_URL, MAX_PLAYER_ITEMS_COUNT, current_users_market
from xenon.spotify3.models import FollowingRequest, PlaybackState, Device, Queue

class GetPlaybackState(GetRequest):
    """ Get information about the user's current playback state, including track or episode, progress, and active device. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-information-about-the-users-current-playback. """
    def __init__(self, market: str = current_users_market()) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player"
        self.api_params = {
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = PlaybackState(self.get_data())        

class TransferPlayback(PutRequest):
    """ Transfer playback to a new device and determine if it should start playing. https://developer.spotify.com/documentation/web-api/reference/#/operations/transfer-a-users-playback. """
    def __init__(self, device_id: str, play: bool = True) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player"
        self.api_params = {}
        self.api_headers = _headers()
        self.api_payload = {
            'device_ids': [device_id]
        }

class GetAvailableDevices(GetRequest):
    """ Get information about a user's available devices. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-a-users-available-devices. """
    def __init__(self) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/players/devices"
        self.api_params = {}
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        devices_list = []
        for device in self.get_data()['devices']:
            devices_list.append(Device(device))
        
        self._data = devices_list

class StartResumePlayback(PutRequest):
    """ Start a new context or resume current playback on the user's active device. https://developer.spotify.com/documentation/web-api/reference/#/operations/start-a-users-playback. """
    def __init__(self, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/play"
        self.api_params = {
            'device_id': device_id
        }
        self.api_headers = _headers()

class PausePlayback(PutRequest):
    """ Pause playback on the user's account. https://developer.spotify.com/documentation/web-api/reference/#/operations/pause-a-users-playback. """
    def __init__(self, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/pause"
        self.api_params = {
            'device_id': device_id
        }
        self.api_headers = _headers()

class SkipToNext(PostRequest):
    """ Skips to next track in the user's queue. https://developer.spotify.com/documentation/web-api/reference/#/operations/skip-users-playback-to-next-track. """
    def __init__(self, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/next"
        self.api_params = {
            'device_id': device_id
        }
        self.api_headers = _headers()

class SkipToPrevious(PostRequest):
    """ Skips to previous track in the user's queue. https://developer.spotify.com/documentation/web-api/reference/#/operations/skip-users-playback-to-previous-track. """
    def __init__(self, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/previous"
        self.api_params = {
            'device_id': device_id
        }
        self.api_headers = _headers()

class SeekToPosition(PutRequest):
    """ Seeks to the given position in the user's currently playing track. https://developer.spotify.com/documentation/web-api/reference/#/operations/seek-to-position-in-currently-playing-track. """
    def __init__(self, position: int, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/seek"
        self.api_params = {
            'position_ms': position,
            'device_id': device_id
        }
        self.api_headers = _headers()

class SetRepeatMode(PutRequest):
    """ Set the repeat mode for the user's playback. Options are repeat-track, repeat-context, and off. https://developer.spotify.com/documentation/web-api/reference/#/operations/set-repeat-mode-on-users-playback. """
    def __init__(self, state: str, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/repeat"
        self.api_params = {
            'state': state,
            'device_id': device_id
        }
        self.api_headers = _headers()

class SetPlaybackVolume(PutRequest):
    """ Set the volume for the user's current playback device. https://developer.spotify.com/documentation/web-api/reference/#/operations/set-volume-for-users-playback. """
    def __init__(self, volume: int, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/volume"
        self.api_params = {
            'volume_percent': volume,
            'device_id': device_id
        }
        self.api_headers = _headers()

class TogglePlaybackShuffle(PutRequest):
    """ Toggle shuffle on or off for user's playback. https://developer.spotify.com/documentation/web-api/reference/#/operations/toggle-shuffle-for-users-playback.  """
    def __init__(self, state: bool, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/shuffle"
        self.api_params = {
            'state': state,
            'device_id': device_id
        }
        self.api_headers = _headers()

class GetRecentlyPlayedTracks(GetRequest):
    """ Get tracks from the current user's recently played tracks. NOTE: Currently doesn't support podcast episodes. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recently-played. """
    def __init__(self, after: int, limit: int = MAX_PLAYER_ITEMS_COUNT) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/recently-played"
        self.api_params = {
            'after': after,
            'limit': limit
        }
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())

class GetCurrentUsersQueue(GetRequest):
    """ Get the list of objects that make up the user's queue. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-queue. """
    def __init__(self) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/queue"
        self.api_params = {}
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = Queue(self.get_data())

class AddItemToPlaybackQueue(PostRequest):
    """ Add an item to the end of the user's current playback queue. https://developer.spotify.com/documentation/web-api/reference/#/operations/add-to-queue. """
    def __init__(self, item_uri: str, device_id: str) -> None:
        super.__init__()

        self.api_url = f"{BASE_URL}/me/player/queue"
        self.api_params = {
            'uri': item_uri,
            'device_id': device_id
        }
        self.api_headers = _headers()
