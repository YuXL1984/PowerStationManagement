# coding: utf-8

from leancloud import Engine
from app import app
from stationdata import StationData
from leancloud import User
import json
engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud! '

@engine.define
#读取所有站点数据
def loadStationData(**params):
    if 'stationName' in params and 'userId' in params:
        funResult = StationData().load_stationData(params['stationName'],params['userId'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def loadStationDataForUserId(**params):
    if 'userId' in params:
        funResult = StationData().load_stationDataForUserId(params['userId'])
        resultDic = {'code':'1000','resultData':funResult}
        return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':{'code':'1001','error':'传入参数错误'}}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def loadSectionStationData(**params):
    if 'page' in params and 'number' in params:
        if int(params['page']) > 0 and int(params['number']) > 0:
            funResult = StationData().load_sectionStationData(int(params['page']),int(params['number']))
            if funResult is '101':
                resultDic = {'code':'1002','resultData':'全部数据分页显示完毕'}
                return json.dumps(resultDic).decode('unicode-escape')
            else:
                resultDic = {'code':'1000','resultData':funResult}
                return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1002','error':'page和number应该为大于0的整数'}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':{'code':'1001','error':'传入参数错误'}}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
#添加站点,传入站点名称和地址,添加后返回站点信息
def addStationData(**params):
    #判断传入参数中是否包含站点名称和站点地址
    if 'stationName' in params and 'stationAddress' in params and 'stationCode' in params and 'positionData' in params :
        funResult = StationData().add_stationData(params['stationName'],params['stationAddress'],params['stationCode'],params['positionData'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'站点名称已存在'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
#添加站点,传入站点名称和地址,添加后返回站点信息
def addStationDataForUserId(**params):
    #判断传入参数中是否包含站点名称和站点地址
    if 'stationName' in params and 'stationAddress' in params and 'stationCode' in params and 'positionData' in params and 'userId' in params:
        funResult = StationData().add_stationDataForUserId(params['stationName'],params['stationAddress'],params['stationCode'],params['positionData'],params['userId'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'站点名称已存在'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def updateStationDataForOid(**params):
    if 'objectId'in params and 'newStationName' in params and 'newStationAddress' in params and 'newStationCode' in params and 'newPositionData' in params:
        funResult = StationData().update_stationDataForOid(params['objectId'],params['newStationName'],params['newStationAddress'],params['newStationCode'],params['newPositionData'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'objectId不正确'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def delStationDataForOid(**params):
    if 'objectId' in params:
        funRequest = StationData().del_stationDataForOid(params['objectId'])
        if funRequest is '100':
            resultDic = {'code':'1000','resultData':'删除成功'}
            return json.dumps(resultDic).decode('unicode-escape')
        elif funRequest is '101':
            resultDic = {'code':'1003','resultData':'objectId不存在'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1002','resultData':'删除失败'}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def searchStationDataForOid(**params):
    if 'objectId' in params:
        funResult = StationData().search_stationDataForOid(params['objectId'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def searchStationDataForName(**params):
    if 'stationName' in params:
        funResult = StationData().search_stationDataForName(params['stationName'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def searchStationDataBlurryForStationName(**params):
    if 'stationName' in params:
        funResult = StationData().search_stationDataBlurryForStationName(params['stationName'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def searchStationDataBlurryForStationCode(**params):
    if 'stationCode' in params:
        funResult = StationData().search_stationDataBlurryForStationCode(params['stationCode'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

@engine.define
def searchStationDataForBlurryFromUserId(**params):
    if 'stationName' in params and 'userId' in params:
        funResult = StationData().search_stationDataForBlurryFromUserId(params['stationName'],params['userId'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return json.dumps(resultDic).decode('unicode-escape')
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return json.dumps(resultDic).decode('unicode-escape')
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return json.dumps(resultDic).decode('unicode-escape')

















