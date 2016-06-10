import loadMongo
import localDataWork
import variable
import demjson
import json

if __name__ == '__main__':
    print "start loading data"
    #loadMongo.loadAccountCard()
    #loadMongo.loadDailyCheckIn()
    #loadMongo.loadUserFile()
    print "finish loading data,start to add up data"
    localDataWork.statisticsClassFile()
    jsonN = {'TANSLATE_CLAZZ': variable.classFileNum[0], 'ENGLISH_CLAZZ': variable.classFileNum[1],
             'GRE_CLAZZ': variable.classFileNum[2]}
    json.dump(jsonN,open('ClassFile.json','w'))

    localDataWork.statisticsClassCheck()
    jsonN = {'TANSLATE_CLAZZ':variable.classCheckTime[0],'ENGLISH_CLAZZ':variable.classCheckTime[1],'GRE_CLAZZ':variable.classCheckTime[2]}
    json.dump(jsonN,open('CheckTime.json','w'))
    print "finish adding up data,start to draw picture"
    #localDataWork.drawFilePicture()
    #localDataWork.drawCheckPicture()
