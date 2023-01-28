
# Import internal modules
from xenon.models import GetRequest
from xenon.spotify3.helpers import _headers, BASE_URL, config_list_to_comma_str, current_users_market
from xenon.spotify3.models import Chapter

class GetChapters(GetRequest):
    def __init__(self, chapter_ids: list, market: str = current_users_market()) -> None:
        super().__init__()

        self.api_url = f"{BASE_URL}/chapters"
        self.api_params = {
            'ids': config_list_to_comma_str(chapter_ids),
            'market': market
        }
        self.api_headers = _headers()

        self.cdq = True
    
    def _config_data(self) -> None:
        """ Configures the data ready to returned to be the caller. """
        chapters_list = []
        for chapter in self.get_data()['chapters']:
            chapters_list.append(Chapter(chapter))

        self._data = chapters_list