
# Import internal modules
from xenon.models import GetRequest
from xenon.spotify3.helpers import _headers, BASE_URL
from xenon.spotify3.models import FollowingRequest

class GetAvailableGenreSeeds(GetRequest):
    """ Retrieve a list of available genres seed parameter values for [recommendations](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations). """
    def __init__(self) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/recommendations/available-genre-seeds"
        self.api_params = {}
        self.api_headers = _headers()