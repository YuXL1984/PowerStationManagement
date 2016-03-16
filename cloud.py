# coding: utf-8

from leancloud import Engine

from app import app


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'

from leancloud import Object

class StationData(Object):
    def save_stationData(self,stationName,stationAddress):
        station_data = StationData()
        station_data.set('stationName',stationName)
        station_data.set('stationAddress',stationAddress)
        station_data.save()
        return station_data.get(id)