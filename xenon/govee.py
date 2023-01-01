
# Import internal modules
from databases import db, GoveeDB
from loggers import govee_logger

import exceptions

class Govee():
    pass

class NewDevice():
    def __init__(self, d_id: str, d_model: str, d_name: str) -> None:
        self.device_id = d_id
        self.device_model = d_model
        self.device_name = d_name

    def commit(self) -> None:
        new_device = GoveeDB()

        new_device.device_id = self.device_id
        new_device.device_model = self.device_model
        new_device.device_name = self.device_name

        try:
            db.session.add(new_device)
            db.session.commit(new_device)

            govee_logger.info(f"Successfully committed device '{self.device_name}' ({self.device_id} : {self.device_model}) to the GoveeDB.")
        except Exception as e:
            raise exceptions.Apis.Govee.FailedToCreateDevice(e, govee_logger)