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

@engine.define
def demo(**params):
    if 'stationName' in params and 'stationAddress' in params:
        station_data = StationData()
        station_data.set('stationName',params['stationName'])
        station_data.set('stationAddress',params['stationAddress'])

        StationData().save_stationData(station_data)


class StationData(Object):

    def save_stationData(self, station_data):
        station_data.save()


#    def update_stationData(self):

