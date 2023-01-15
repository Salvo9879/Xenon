
# Import internal modules
from xenon.loggers import xenon_requests
from xenon.exceptions import http_exceptions

# Import external modules
import requests
import json

class GetRequest():
    """ 
    Add this class as an inheritance for all api get requests of Xenon. Some api's may return errors so please use the structure when making api calls: 

    ---
    ``` python
    ngr = GetRequest(api_url, api_params, api_headers)
    ngr.create_request()

    if ngr.code != 200:
        # Api has failed to retrieve data
        return 

    # This code will run if the Api has successfully returned the data

    ```
    """


    def __init__(self, api_url: str = '', api_params: dict = {}, api_headers: dict = {}, cdq: bool = False) -> None:
        self.api_url: str = api_url
        self.api_params: dict = api_params
        self.api_headers: dict = api_headers
        
        self.code: int = None
        self._data: dict = None

        self.cdq = cdq

    def create_request(self) -> None:
        """ Deploys the request at this stage. The urls, parameters & headers are sent of with it. If `self.cdq` (config_data_query) is set to `True` then it calls `self._config_data()`. This however
        will have to be created on the main object instead of this one """

        r = requests.get(url=self.api_url, params=self.api_params, headers=self.api_headers)

        self.code = r.status_code
        self._data = r.json()

        if self.code == 200:
            if self.cdq:
                self._config_data()

    def _get_data_by_identifier(self, data: dict, obj: object, identifier: str, value: any, mode: str = 'all') -> None:
        """ Gets certain data by an identifier of a dict. Iterates through the dict (`data`) and if the value of the key is equal to `identifier` then formats the data using an object (`obj`) it 
        either appends this to a list or returns it straight to the call function. This is dependant of if parameter `mode` is equal to `all` or `first`. """

        data_list = []
        for data_attr in data:
            if data_attr[identifier] == value:
                if mode == 'first':
                    return obj(data_attr)
                data_list.append(obj(data_attr))
        return data_list

    def get_data(self) -> dict:
        """ Returns the whole data package of the object. This should be used instead of `self._data`. """
        return self._data

class PutRequest():
    def __init__(self, api_url: str = '', api_params: dict = {}, api_headers: dict = {}, api_payload: dict = {}) -> None:
        self.api_url: str = api_url
        self.api_params: dict = api_params
        self.api_headers: dict = api_headers
        self.api_payload: dict = api_payload

        self.code: int = None
        self._data: dict = None

    def create_request(self) -> None:
        r = requests.put(url=self.api_url, params=self.api_params, headers=self.api_headers, data=json.dumps(self.api_payload))

        self.code = r.status_code
        self._data = r.text

class DeleteRequest():
    def __init__(self, api_url: str = '', api_params: dict = {}, api_headers: dict = {}) -> None:
        self.api_url: str = api_url
        self.api_params: dict = api_params
        self.api_headers: dict = api_headers

        self.code: int = None
        self._data: dict = None

    def create_request(self) -> None:
        r = requests.delete(url=self.api_url, params=self.api_params, headers=self.api_headers)

        self.code = r.status_code
        self._data = r.text

class ObjectScaffold():
    def __init__(self, data: dict) -> None:
        self._data = data

    def get_data(self):
        return self._data