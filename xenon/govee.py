from .databases import Apis

class Govee():
    govee_row = Apis.query.filter_by(api_name='govee').first()