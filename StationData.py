# coding: utf-8

from leancloud import Object
from leancloud import Query

class StationData(Object):

    def add_stationData(self, add_station_data):
        add_station_data.save()
        return  add_station_data.get('stationNumber')
        # return add_station_data.id

    def del_stationData(self,del_station_data):
        del_station_data.destroy()
        return '1000'

    def searchFromId(self,objectId):
        query = Query(StationData)
        data_score = query.get(objectId)
        requestDic = {'stationNumber':data_score.get('stationNumber'),'stationName':data_score.get('stationName'),'stationAddress':data_score.get('stationAddress')}
        return requestDic

    def readStationData(self):
        result = Query.do_cloud_query('select * from StationData')
        # results 是查询返回的结果，Object 列表
        results = result.results
        station_list = []
        for item in results:
            station_list.append((item.get('objectID'),item.get('stationNumber'), item.get('stationName'), item.get('stationAddress')))
        station_key = ('objectID','stationNumber', 'stationName', 'stationAddress')
        requestDic = map(lambda x: dict(zip(station_key, x)), station_list)
        return requestDic









#    def update_stationData(self):
