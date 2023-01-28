
# Import internal modules
from xenon.models import GetRequest
from xenon.spotify3.helpers import _headers, BASE_URL
from xenon.spotify3.models import FollowingRequest

class GetBrowsingCategories(GetRequest):
    """ Get a list of categories used to tag items in Spotify (on, for example, the Spotify player's “Browse” tab). """
    def __init__(self, category_id: str) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/browse/categories/{category_id}"
        self.api_params = {}
        self.api_headers = _headers()

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        self._data = FollowingRequest(self.get_data())