import loadMongo
import localDataWork

if __name__ == '__main__':
    print "start loading data"
    #loadMongo.loadAccountCard()
    #loadMongo.loadDailyCheckIn()
    #loadMongo.loadUserFile()
    print "finish loading data,start to add up data"
    localDataWork.statisticsClassFile()
    localDataWork.statisticsClassCheck()
    print "finish adding up data,start to draw picture"
    localDataWork.drawFilePicture()
    localDataWork.drawCheckPicture()
