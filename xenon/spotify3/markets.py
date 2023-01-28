
# Import internal modules
from xenon.models import GetRequest
from xenon.spotify3.helpers import _headers, BASE_URL, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import Chapter

class GetAvailableMarkets(GetRequest):
    """ Get the list of markets where Spotify is available. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-available-markets. """
    def __init__(self) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/markets"
        self.api_params = {}
        self.api_headers = _headers()