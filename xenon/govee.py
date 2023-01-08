
# Import internal modules
from xenon.models import GetRequest, PutRequest



#* ====================================================================================================================================================================================================



class _Urls():
    GET_URL = 'https://developer-api.govee.com/v1/devices'
    PUT_URL = 'https://developer-api.govee.com/v1/devices/control'



#* ====================================================================================================================================================================================================



class GoveeDevice():
    def __init__(self, data: dict) -> None:
        self._data = data

    def get_data(self) -> dict:
        """ Returns the whole data package of the object. """
        return self._data

    def _get_supported_cmds(self) -> list:
        """ Returns a list of the supported cmds. """
        return self.get_data()['supportCmds']

    @property
    def mac_addr(self) -> str:
        """ Mac address of your device. Use device and model to identify the target one device. """
        return self.get_data()['device']

    @property
    def model(self) -> str:
        """ Returns the product model of your device. """
        return self.get_data()['model']

    @property
    def is_controllable(self) -> bool:
        """ Returns `True` if the device is controllable. Controllable will be true when the device support commands to control. """
        return self.get_data()['controllable']

    @property
    def is_retrievable(self) -> bool:
        """ Returns `True` if the device is retrievable. Retrievable will be true when the device support querying the current device state. """
        return self.get_data()['retrievable']

    @property
    def supports_turn_cmd(self) -> bool:
        """ Returns `True` if the device supports the `turn` cmd. """
        return 'turn' in self._get_supported_cmds()

    @property
    def supports_brightness_cmd(self) -> bool:
        """ Returns `True` if the device supports the `brightness` cmd. """
        return 'brightness' in self._get_supported_cmds()

    @property
    def supports_color_cmd(self) -> bool:
        """ Returns `True` if the device supports the `color` cmd. """
        return 'color' in self._get_supported_cmds()

    @property
    def supports_color_temperature_cmd(self) -> bool:
        """ Returns `True` if the device supports the `colorTem` cmd. """
        return 'colorTem' in self._get_supported_cmds()

    @property
    def temperature_range(self) -> dict:
        """ Returns the temperature range of the device. """
        return self.get_data()['properties']['colorTem']['range']



#* ====================================================================================================================================================================================================



class GetDevicesRequest(GetRequest):
    def __init__(self, api_key: str) -> None:
        super().__init__()

        self.api_url = _Urls.GET_URL
        self.api_params = {}
        self.api_headers = {
            'Govee-API-Key': api_key
        }

        self.cdq = True

    def _config_data(self) -> None:
        """ Configures the data gathered from the request api. This essentially removes any unnecessary data. """
        self._data = self._data['data']['devices']

    def get_all_devices(self) -> list:
        """ Gets all the devices linked to the account. """
        devices = []
        for device in self.get_data():
            devices.append(GoveeDevice(device))

        return devices

    def get_device_by_mac_addr(self, mac_addr: str, mode: str = 'first') -> GoveeDevice:
        """ Returns device/s based on a `mac_addr`. """
        return self._get_data_by_identifier(self.get_data(), GoveeDevice, 'device', mac_addr, mode)

    def get_device_by_model(self, model: str, mode: str = 'all') -> GoveeDevice:
        """ Returns device/s based on the `model`. """
        return self._get_data_by_identifier(self.get_data(), GoveeDevice, 'model', model, mode)

    def get_controllable_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Returns device/s that are `controllable`. """
        return self._get_data_by_identifier(self.get_data(), GoveeDevice, 'controllable', True, mode)

    def get_device_by_name(self, name: str, mode: str = 'first') -> GoveeDevice:
        """ Returns device/s based on a `name`. """
        return self._get_data_by_identifier(self.get_data(), GoveeDevice, 'deviceName', name, mode)

    def get_retrievable_devices(self, mode: str = 'all') -> GoveeDevice:
        """ Returns device/s that are 'retrievable'. """
        return self._get_data_by_identifier(self.get_data(), GoveeDevice, 'retrievable', True, mode)

    def get_support_cmd_devices(self, cmd: str):
        """ Returns device/s that support `cmds`. """
        return cmd in self.get_data()['supportCmds']

class PutDevicesRequest(PutRequest):
    def __init__(self, api_key: str, device: GoveeDevice) -> None:
        super().__init__()

        self.api_url = _Urls.PUT_URL
        self.api_params = {}
        self.api_header = {
            'Govee-API-Key': api_key,
            'Content-Type': 'application/json'
        }
        self.api_payload = {
            "device": device.mac_addr,
            "model": device.model,
            "cmd": {
                "name": None,
                "value": None
            }
        }

    def api_payload_name(self, name: str = None) -> None:
        """ Alters the payload name (`self.api_payload['cmd']['name']`) to parameter `name`. """
        self.api_payload['cmd']['name'] = name

    def api_payload_value(self, value: str = None) -> None:
        """ Alters the payload name (`self.api_payload['cmd']['value']`) to parameter `value`. """
        self.api_payload['cmd']['value'] = value

    def turn_on(self) -> None:
        """ Turns the device on. """
        self.api_payload_name('turn')
        self.api_payload_value('on')

    def turn_off(self) -> None:
        """ Turns the device off. """
        self.api_payload_name('turn')
        self.api_payload_value('off')

    def change_brightness(self, value: int) -> None:
        """ Changes the devices brightness to parameter `value`. If `value` is greater than `255` or less than `0` a `ValueError()` is raised. """
        if value > 100 or value < 0:
            raise ValueError('Parameter \'value\' cannot be greater than 100, or less than 0')

        self.api_payload_name('brightness')
        self.api_payload_value(value)

    def change_color(self, color: tuple) -> None:
        """ Changes the devices color to parameter `color`. This is a tuple of 3 values. Each represent a sector of the color model - RGB. If any of these values are greater than `255` or less than
        `0` a `ValueError() is raised. """
        for c in color:
            if c > 255 or c < 0:
                raise ValueError('Parameter \'color\' has a value greater than 255 or less than 0') 

        self.api_payload_name('color')
        self.api_payload_value({'r': color[0], 'g': color[1], 'b': color[2]})

    def change_color_temperature(self, value: int) -> None:
        """ Changes the color temperature of the device. The range of this varies based on device, however ranges can be found via `GoveeDevice.temperature_range`. """

        self.api_payload_name('colorTem')
        self.api_payload_value(value)
