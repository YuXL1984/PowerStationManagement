# coding: utf-8

from leancloud import Engine
from leancloud import Object

from app import app


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'



class StationData(Object):
    def save_stationData(**params):
        station_data = StationData()
        station_data.set('stationName',params['stationName'])
        station_data.set('stationAddress',params['stationAddress'])
        station_data.save()
        return station_data.get(id)