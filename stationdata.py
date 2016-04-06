# coding: utf-8

from leancloud import Object
from leancloud import Query


class StationData(Object):

    def load_stationData(self):
        queryResult = Query.do_cloud_query('select * from StationData')
        resultObjests = queryResult.results
        stationData_list = []
        for object in resultObjests:
            stationData_list.append((object.id, object.get('stationNumber'), object.get('stationName'), object.get('stationAddress')))
        station_key = ('objectId', 'stationNumber', 'stationName', 'stationAddress')
        resultDic = map(lambda x: dict(zip(station_key, x)), stationData_list)
        return resultDic

    def load_sectionStationData(self, page, number):
        skip = (page - 1) * number
        StationData = Object.extend('StationData')
        query = Query(StationData)
        query.skip(skip)
        query.limit(number)
        resultObjests = query.find()
        #如果结果存在
        if resultObjests:
            #将结果保存至resultDic
            stationData_list = []
            for object in resultObjests:
                stationData_list.append((object.id, object.get('stationNumber'), object.get('stationName'), object.get('stationAddress')))
            station_key = ('objectId', 'stationNumber', 'stationName', 'stationAddress')
            resultDic = map(lambda x: dict(zip(station_key, x)), stationData_list)
            return resultDic
        else:
            return '101'

    def add_stationData(self, stationName,stationAddress):
        funResult = StationData().search_stationDataForName(stationName)
        if funResult is '101':
            add_station_data = StationData()
            add_station_data.set('stationName',stationName)
            add_station_data.set('stationAddress',stationAddress)
            add_station_data.save()
            resultDic = {'objectId':add_station_data.id,'stationNumber':add_station_data.get('stationNumber'),'stationName':add_station_data.get('stationName'),'stationAddress':add_station_data.get('stationAddress')}
            return resultDic
        else:
            return '101'

    def update_stationDataForOid(self,objectId,newStationName,newStationAddress):
        #根据Oid查询目前值
        funResult = self.search_stationDataForOid(objectId)
        resultDic = funResult[0]
        if funResult != '101':
            #判断新站点名称是否改变
            if resultDic['stationName'] != newStationName:
                #如果改变进行更新
                queryResult = Query.do_cloud_query('update StationData set stationName = ?  where objectId = ?',newStationName,objectId)
            #判断新站点地址是否改变
            if resultDic['stationAddress'] != newStationAddress:
                #如果改变进行更新
                queryResult = Query.do_cloud_query('update StationData set stationAddress = ?  where objectId = ?',newStationAddress,objectId)
            funResult = self.search_stationDataForOid(objectId)
            #返回更新后的值
            return funResult
        else:
            #找不到Oid
            return '101'

    def del_stationDataForOid(self,objectId):
        #搜索oId是否存在
        funResult = self.search_stationDataForOid(objectId)
        #!=101代表search_stationDataForOid方法搜索有结果
        if funResult != '101':
            #删除该对象
            resultData = Query.do_cloud_query('delete from StationData where objectId = ?',objectId)
            #删除后再次搜索
            funResult = self.search_stationDataForOid(objectId)
            #如果搜索无结果
            if funResult is '101':
                #返回删除成功
                return '100'#成功,搜索无结果
            else:
                return '102'#失败,搜索有结果
        else:
            #objectId没有找到
            return '101'

    def search_stationDataForOid(self,objectId):
        #使用CQL语句查询
        queryResult = Query.do_cloud_query('select * from StationData where objectId = ?',objectId)
        #接收查询结果
        resultObjests = queryResult.results
        #如果结果存在
        if resultObjests:
            #将结果保存至resultDic
            stationData_list = []
            for object in resultObjests:
                stationData_list.append((object.id, object.get('stationNumber'), object.get('stationName'), object.get('stationAddress')))
            station_key = ('objectId', 'stationNumber', 'stationName', 'stationAddress')
            resultDic = map(lambda x: dict(zip(station_key, x)), stationData_list)
            return resultDic
        else:
            return '101'

    def search_stationDataForName(self,stationName):
        StationData = Object.extend('StationData')
        query = Query(StationData)
        #查询条件
        query.equal_to('stationName',stationName)
        #接收查询结果
        resultObjests = query.find()
        #如果结果存在
        if resultObjests:
            #将结果保存至resultDic
            stationData_list = []
            for object in resultObjests:
                stationData_list.append((object.id, object.get('stationNumber'), object.get('stationName'), object.get('stationAddress')))
            station_key = ('objectId', 'stationNumber', 'stationName', 'stationAddress')
            resultDic = map(lambda x: dict(zip(station_key, x)), stationData_list)
            return resultDic
        else:
            return '101'

    def search_stationDataForBlurry(self,stationName):
        #使用CQL语句查询
        #queryResult = Query.do_cloud_query('select * from StationData where stationName like "%?%"', stationName)
        queryResult = Query.do_cloud_query('select * from StationData where stationName like "%'+ stationName +'%"')
        #接收查询结果
        resultObjests = queryResult.results
        #如果结果存在
        if resultObjests:
            #将结果保存至resultDic
            stationData_list = []
            for object in resultObjests:
                stationData_list.append((object.id, object.get('stationNumber'), object.get('stationName'), object.get('stationAddress')))
            station_key = ('objectId', 'stationNumber', 'stationName', 'stationAddress')
            resultDic = map(lambda x: dict(zip(station_key, x)), stationData_list)
            return resultDic
        else:
            return '101'



