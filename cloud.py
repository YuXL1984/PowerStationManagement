# coding: utf-8

from leancloud import Engine
from app import app
from stationdata import StationData
from leancloud import User

engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud! '

@engine.define
#读取所有站点数据
def loadStationData():
    print '===========> loadStationData'
    funResult = StationData().load_stationData()
    resultDic = {'code':'1000','resultData':funResult}
    return funResult

@engine.define
def loadSectionStationData(**params):
    if 'page' in params and 'number' in params:
        if int(params['page']) > 0 and int(params['number']) > 0:
            funResult = StationData().load_sectionStationData(int(params['page']),int(params['number']))
            if funResult is '101':
                resultDic = {'code':'1002','resultData':'全部数据分页显示完毕'}
                return resultDic
            else:
                resultDic = {'code':'1000','resultData':funResult}
                return resultDic
        else:
            resultDic = {'code':'1002','error':'page和number应该为大于0的整数'}
            return resultDic
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic

@engine.define
#添加站点,传入站点名称和地址,添加后返回站点信息
def addStationData(**params):
    #判断传入参数中是否包含站点名称和站点地址
    if 'stationName' in params and 'stationAddress' in params:
        funResult = StationData().add_stationData(params['stationName'],params['stationAddress'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'站点名称已存在'}
            return resultDic
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return resultDic
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic

@engine.define
def updateStationDataForOid(**params):
    if 'objectId'in params and 'newStationName' in params and 'newStationAddress' in params:
        funResult = StationData().update_stationDataForOid(params['objectId'],params['newStationName'],params['newStationAddress'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'objectId不正确'}
            return resultDic
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return resultDic
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic

@engine.define
def delStationDataForOid(**params):
    if 'objectId' in params:
        funRequest = StationData().del_stationDataForOid(params['objectId'])
        if funRequest is '100':
            resultDic = {'code':'1000','resultData':'删除成功'}
            return resultDic
        elif funRequest is '101':
            resultDic = {'code':'1003','resultData':'objectId不存在'}
            return resultDic
        else:
            resultDic = {'code':'1002','resultData':'删除失败'}
            return resultDic
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic

@engine.define
def searchStationDataForOid(**params):
    if 'objectId' in params:
        funResult = StationData().search_stationDataForOid(params['objectId'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return resultDic
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return resultDic
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic

@engine.define
def searchStationDataForName(**params):
    if 'stationName' in params:
        funResult = StationData().search_stationDataForName(params['stationName'])
        if funResult is '101':
            resultDic = {'code':'1002','error':'搜索无结果'}
            return resultDic
        else:
            resultDic = {'code':'1000','resultData':funResult}
            return resultDic
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic

@engine.define
def useRegister(**params):
    if 'userName' in params and 'userPassword' in params and 'userEmail' in params:
        user = User()
        user.set("username",params['userName'])
        user.set("password",params['userPassword'])
        user.set("email",params['userEmail'])
        user.sign_up()
        return '100'
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic

@engine.define
def useLogin(**params):
    if 'userName' in params and 'userPassword' in params:
        User().login(params['userName'], params['userPassword'])
        return '100'
    else:
        resultDic = {'code':'1001','error':'传入参数错误'}
        return resultDic






















