
# Import external modules
import requests
import json

GOVEE_API_GET_URL = 'https://developer-api.govee.com/v1/devices'
GOVEE_API_PUT_URL = 'https://developer-api.govee.com/v1/devices/control'

class GoveeDevice():
    """ Class which configures all Govee Devices. This makes it easier to get information about certain devices. """

    def __init__(self, data: dict) -> None:
        self.data = data
        self.cmd = data['supportCmds']

    def __repr__(self) -> str:
        return f"[ {self.device_name} ] - MODEL: {self.model} - DEVICE ID: {self.device_id}"

    @property
    def device_id(self) -> str:
        """ Gets the device id (`device`). """
        return self.data['device']

    @property
    def model(self) -> str:
        """ Gets the device model (`model`). """
        return self.data['model']

    @property
    def device_name(self) -> str:
        """ Gets the device name (`deviceName`). """
        return self.data['deviceName']

    @property
    def is_controllable(self) -> str:
        """ Returns `True` if the device is controllable (`controllable`). """
        return self.data['controllable']

    @property
    def is_retrievable(self) -> str:
        """ Returns `True` if the device is retrievable (`retrievable`). """
        return self.data['retrievable']

    @property
    def supports_turn(self) -> bool:
        """ Returns `True` if the device supports the `turn` command (`devices.supportCmds.turn`). """
        return 'turn' in self.cmd

    @property
    def supports_brightness(self) -> bool:
        """ Returns True if the device supports the `brightness` command (`devices.supportCmds.brightness`). """
        return 'brightness' in self.cmd

    @property
    def supports_color(self) -> bool:
        """ Returns `True` if the device supports the `color` command (`devices.supportCmds.color`) """
        return 'color' in self.cmd

    @property
    def supports_temperature(self) -> bool:
        """ Returns True if the device supports the `colorTem` command (`devices.supportCmds.colorTem`) """
        return 'colorTem' in self.cmd

    @property
    def temperature_range(self) -> dict:
        """ Returns the `temperature range` of the device (`devices.properties.colorTem.range`). """
        return self.data['properties']['colorTem']['range']

class NewGetRequest():
    """ Class to create a new get request. """

    def __init__(self, api_key: str) -> None:
        self.api_url = GOVEE_API_GET_URL
        self.api_key = api_key
        self.api_headers = {'Govee-API-Key':self.api_key}

        self._device_data = None
        self.message = None
        self.code = None

    def __repr__(self) -> str:
        return f"[ {self.code} ] - {self.message}"

    def create_request(self) -> None:
        """ Function which configures the request with the url & headers. The returned status code & message is then assigned to attributes `self.code` & `self.message`. """

        # TODO: Create helper which blocks requests made from a unauthorized user & logger.

        r = requests.get(url=self.api_url, headers=self.api_headers).json()

        self._device_data = r['data']['devices']
        self.message = r['message']
        self.code = r['code']

    def get_all_devices(self) -> dict:
        """ Returns all the devices the api request collected. """

        return self._device_data

    def _get_device_by_identifier(self, identifier: str, value: any, mode: str = 'first') -> GoveeDevice:
        """ Gets devices by an identification.
        Supported identification values:
        - `device`
        - `model`
        - `deviceName`
        - `controllable`
        - `retrievable`
        - `supportCmds`

        The param `value` is then used to see if the value of any of the identification matches. 

        If param `mode` is equal to `first` then the function will return a `GoveeDevice()` object of the first device which match the identification. 
        If param `mode` is qual to `all` then the function will return a `list` of all the devices that match the identification.

        This function should not be called outside of the object. 

        """

        applied_devices = []
        for device in self._device_data:
            if identifier == 'cmd':
                if value in device['supportCmds']:
                    if mode == 'all':
                        applied_devices.append(GoveeDevice(device))
                        continue
                    return GoveeDevice(device)
            if device[identifier] == value:
                if mode == 'all':
                    applied_devices.append(GoveeDevice(device))
                    continue
                return GoveeDevice(device)

        return applied_devices


    def get_devices_by_id(self, value: any, mode: str = 'first') -> GoveeDevice:
        """ Gets devices based on the `id`. """
        return self._get_device_by_identifier('device', value, mode)

    def get_devices_by_model(self, model: any, mode: str = 'first') -> GoveeDevice:
        """ Gets devices based on the `model`. """
        return self._get_device_by_identifier('model', model, mode)

    def get_devices_by_name(self, name: any, mode: str = 'first') -> GoveeDevice:
        """ Gets devices based on the `name`. """
        return self._get_device_by_identifier('deviceName', name, mode)


    def get_controllable_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Gets devices based on the whether they are `controllable`. """
        return self._get_device_by_identifier('controllable', True, mode)

    def get_retrievable_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Gets devices based on whether they are `retrievable`. """
        return self._get_device_by_identifier('retrievable', True, mode)
    

    def get_turn_supported_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Gets devices based on whether they support the `turn` cmd. """
        return self._get_device_by_identifier('cmd', 'turn', mode)

    def get_brightness_supported_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Gets devices based on whether they support the `brightness` cmd. """
        return self._get_device_by_identifier('cmd', 'brightness', mode)

    def get_color_supported_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Gets devices based on whether they support the `color` cmd. """
        return self._get_device_by_identifier('cmd', 'color', mode)

    def get_temperature_supported_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Gets devices based on whether they support the `temperature` cmd. """
        return self._get_device_by_identifier('cmd', 'colorTem', mode)

class NewPutRequest():
    """ Class to create a new put request. """

    def __init__(self, api_key: str, device: GoveeDevice) -> None:
        self.api_url = GOVEE_API_PUT_URL
        self.api_key = api_key
        self.api_headers = {'Govee-API-Key':self.api_key, 'Content-Type':'application/json'}

        self.device = device

        self.name = None
        self.value = None
        self.payload = None

        self.message = None
        self.code = None

    def __repr__(self) -> str:
        return f"[ {self.code} ] - {self.message}"

    def create_request(self) -> None:
        """ Function which configures the request with the url, headers & payload. 
        If the payload is not configured, i.e., a command function has not been called, then it will raise an attribute error.  
        The returned status code & message is then assigned to the attributes `self.code` & `self.message`. """

         # TODO: Create helper which blocks requests made from a unauthorized user & logger.

        if not self.payload:
            raise AttributeError('Request was rejected due to empty payload')

        r = requests.put(url=self.api_url, headers=self.api_headers, data=json.dumps(self.payload)).json()

        self.message = r['message']
        self.code = r['code']

    def update_payload(self) -> None:
        """ Updates the attribute `self.payload`. This should be called after every command function is called. """

        self.payload = {
            'device': self.device.device_id,
            'model': self.device.model,
            'cmd': {
                'name': self.name,
                'value': self.value
            }
        }

    def turn_device_on(self) -> None:
        """ Command function which turns the device `on`. """

        self.name = 'turn'
        self.value = 'on'
        self.update_payload()

    def turn_device_off(self) -> None:
        """ Command function which turns the device `off`. """

        self.name = 'turn'
        self.value = 'off'
        self.update_payload()

    def change_brightness(self, value: float) -> None:
        """ Command function which turns the device brightness to param `value`.
        If `value` is bigger then `100` or smaller than `0`, then a `ValueError` is raised. """

        if value > 100 or value < 0:
            raise ValueError('Expected a number between 0 & 100')

        self.name = 'brightness'
        self.value = value
        self.update_payload()

    def change_color(self, color: tuple) -> None:
        """ Command function which turns the device color. Takes in param `color` as a tuple which represents RBG values - `(r, g, b)`. If any one of these values are higher than `255` or lower than `0`, a `ValueError` is raised. """

        for c in color:
            if c > 255 or c < 0:
                raise ValueError('Expected a number between 0 & 255')

        color_data = {'r': color[0], 'g': color[1], 'b': color[2]}

        self.name = 'color'
        self.value = color_data
        self.update_payload()

    def change_temperature(self, value: float) -> None:
        """ Command function which turns the device temperature to param `value`. """

        self.name = 'colorTem'
        self.value = value
        self.update_payload()