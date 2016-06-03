# -*- coding: utf-8 -*-
import leancloud
from leancloud import Object,Query

leancloud.init('kw5bydfai9pkz7elxibpe5clhtrrhpgya7e3m7wx8cwvyqub','d5wcjea7kapo3aqn1222kvzqdp2bkyk7s93qlcybi6oaenuu')


class AccountCard(Object):
    @property
    def card(self):
        return self.get('card')

    @property
    def clazzKey(self):
        return self.get('clazzKey')

    @property
    def isPublish(self):
        return self.get('isPublish')

    @property
    def openId(self):
        return self.get('openId')

class UserFile(Object):
    @property
    def fileType(self):
        return self.get('fileType')

    @property
    def openId(self):
        return self.get('openId')

class DailyCheckIn(Object):
    @property
    def checkTime(self):
        return self.get('checkTime')

    @property
    def openId(self):
        return self.get('openId')

Account_card = Object.extend('AccountCard')
queryCard = Query(Account_card)
User_file = Object.extend('UserFile')
queryFile = Query(User_file)
Daily_checkIn = Object.extend('DailyCheckIn')
queryCheckIn = Query(Daily_checkIn)

FileToNum = {'voice':0, 'image':1, 'video':2, 'shortvideo':3}
ClassToNum = {'TANSLATE_CLAZZ':0, 'ENGLISH_CLAZZ':1, 'GRE_CLAZZ':2}

cols = 4
rows = 3
classFileNum = [[0 for col in range(cols)]for row in range(rows)]
cols = 48
rows = 3
classCheckTime = [[0 for col in range(cols)]for row in range(rows)]

lostNum = 0
num = 0


def statisticsClassFileType(id,fileType):

    global lostNum
    global classFileNum
    # global num
    queryCard.equal_to('openId', id)
    user = queryCard.find()
    if (user.__len__() != 0):
        user = user[0]
        classType = user.clazzKey.encode('utf-8')
        classFileNum[ClassToNum[classType]][FileToNum[fileType]] += 1
    else:
        lostNum += 1

def statisticsClassCheckTime(id,hour,monment):

    global classCheckTime
    global lostNum
    global num

    queryCard.equal_to('openId',id)
    user =  queryCard.find()
    if (user.__len__() != 0):
        user = user[0]
        classType = user.clazzKey.encode('utf-8')
        classCheckTime[ClassToNum[classType]][hour * 2 + monment % 30] += 1
    else:
        lostNum += 1

    #print classCheckTime
    print num
    num += 1


def statisticsClassFile():

    queryFile.limit(1000)
    useData = queryFile.find()

    skipNum = 0
    while useData.__len__() > 0:
        for each in useData:
            id = each.openId.encode('utf-8')
            fileType = each.fileType.encode('utf-8')
            statisticsClassFileType(id,fileType)

        skipNum += 1
        queryFile.skip(skipNum * 1000)
        useData = queryFile.find()


def statisticsClassCheck():

    queryCheckIn.limit(1000)
    queryCheckIn.equal_to('openId','ogLsCwZeWeIqY9KBNjoK4lOFSoR4')
    useData = queryCheckIn.find()

    skipNum = 0
    while useData.__len__() > 0:
        for each in useData:
            id = each.openId.encode('utf-8')
            checkTime = str(each.checkTime)
            hour = int(checkTime[11:13])
            monment = int(checkTime[14:16])

            if monment < 15:
                monment = 0
            elif monment < 30:
                monment = 30
            elif monment < 45:
                monment = 30
            else:
                monment = 0
                hour = (hour + 1) % 24
            statisticsClassCheckTime(id,hour,monment)

    skipNum += 1
    queryFile.skip(skipNum * 1000)
    useData = queryFile.find()

if __name__ == '__main__':

    statisticsClassCheck()
