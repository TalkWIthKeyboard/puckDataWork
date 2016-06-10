#coding=utf-8
import pymongo
import json
import variable

client = pymongo.MongoClient("localhost",27017)
db = client.test

def loadAccountCard():
    f = file('AccountCard.json')
    data = json.load(f)
    data = data['results']
    collect = db.AccountCard

    for each in data:
        card = each['card']
        openId = each['openId'].encode('utf-8')
        isPublish = each['isPublish']
        clazzKey = each['clazzKey'].encode('utf-8')
        eachData = {'card':card,'openId':openId,'isPublish':isPublish,'clazzKey':clazzKey}
        collect.insert(eachData)

def loadDailyCheckIn():
    f = file('DailyCheckIn.json')
    data = json.load(f)
    data = data['results']
    collect = db.DailyCheckIn

    for each in data:
        createdAt = each['checkTime']['iso'].encode('utf-8')[0:10]
        if createdAt == variable.nowDay:
            checkTime = each['checkTime']['iso'].encode('utf-8')
            openId = each['openId'].encode('utf-8')
            eachData = {'checkTime':checkTime,'openId':openId}
            collect.insert(eachData)

def loadUserFile():
    f = file('UserFile.json')
    data = json.load(f)
    data = data['results']
    collect = db.UserFile

    for each in data:
        createdAt = each['createdAt'].encode('utf-8')[0:10]
        if createdAt == variable.nowDay:
            openId = each['openId'].encode('utf-8')
            fileType = each['fileType'].encode('utf-8')
            eachData = {'openId':openId,'fileType':fileType}
            collect.insert(eachData)

def loadAccount():
    f = file('Account.json')
    data = json.load(f)
    data = data['results']
    collect = db.Account

    for each in data:
        isVerify = each['isVerify']
        if (isVerify):
            openId = each['openId'].encode('utf-8')
            clazzKey = each['clazzKey'].encode('utf-8')
            eachData = {'openId':openId,'clazzKey':clazzKey}
            collect.insert(eachData)

if __name__ == '__main__':
    loadAccountCard()
    print ('finish 1')
    loadDailyCheckIn()
    print ('finish 2')
    loadUserFile()
    print ('finish 3')
    loadAccount()
    print ('finish 4')