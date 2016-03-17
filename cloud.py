# coding: utf-8

from leancloud import Engine
from app import app
from stationdata import StationData

engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'

@engine.define
def addData(**params):
    if 'stationName' in params and 'stationAddress' in params:
        add_station_data = StationData()
        add_station_data.set('stationName',params['stationName'])
        add_station_data.set('stationAddress',params['stationAddress'])
        station_number = StationData().add_stationData(add_station_data)
        return station_number

@engine.define
def delData(**params):
    if 'stationName' in params:
        del_station_data = StationData()
        del_station_data.set('stationName',params['stationName'])
        funRequest = StationData().del_stationData(del_station_data)
        return funRequest

@engine.define
def searchForId(**params):
    objectId = params['objectId']
    funRequest = StationData().searchFromId(objectId)
    return funRequest

@engine.define
def readData():
    funRequest = StationData().readStationData()
    return funRequest


































