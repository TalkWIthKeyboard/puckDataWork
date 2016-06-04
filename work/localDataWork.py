import pymongo
import matplotlib.pyplot as plt
import variable

client = pymongo.MongoClient("localhost",27017)
db = client.test

FileToNum = {'voice':0, 'image':1, 'video':2, 'shortvideo':3}
ClassToNum = {'TANSLATE_CLAZZ':0, 'ENGLISH_CLAZZ':1, 'GRE_CLAZZ':2}
NumToClass = {0:'TANSLATE_CLAZZ', 1:'ENGLISH_CLAZZ', 2:'GRE_CLAZZ'}

def statisticsClassFileType(id,fileType):
    collect = db.AccountCard
    data = collect.find_one({'openId':id})
    if data:
        clazzKey = data['clazzKey'].encode('utf-8')
        variable.classFileNum[ClassToNum[clazzKey]][FileToNum[fileType]] += 1
    else:
        variable.lostNum += 1

def statisticsClassCheckTime(id,hour):

    collect = db.AccountCard
    data = collect.find_one({'openId':id})
    if data:
        clazzKey = data['clazzKey'].encode('utf-8')
        variable.classCheckTime[ClassToNum[clazzKey]][hour] += 1
    else:
        variable.lostNum += 1


def statisticsClassFile():
    collect = db.UserFile
    for each in collect.find():
        id = each['openId'].encode('utf-8')
        fileType = each['fileType'].encode('utf-8')
        statisticsClassFileType(id,fileType)

def statisticsClassCheck():
    collect = db.DailyCheckIn
    for each in collect.find():
        id = each['openId'].encode('utf-8')
        checkTime = str(each['checkTime'])
        hour = int(checkTime[11:13]) % 24
        monment = int(checkTime[14:16])

        if monment > 30:
            hour = (hour + 1) % 24
        statisticsClassCheckTime(id, hour)

def drawFilePicture():
    plt.figure(1)
    ax1 = plt.subplot(131)
    ax2 = plt.subplot(132)
    ax3 = plt.subplot(133)

    labels = ['voice', 'image', 'video', 'shortvideo']

    plt.sca(ax1)
    plt.pie(variable.classFileNum[0], labels=labels, labeldistance=1.1, autopct='%3.1f%%', startangle=90)
    plt.sca(ax2)
    plt.pie(variable.classFileNum[1], labels=labels, labeldistance=1.1, autopct='%3.1f%%', startangle=90)
    plt.sca(ax3)
    plt.pie(variable.classFileNum[2], labels=labels, labeldistance=1.1, autopct='%3.1f%%', startangle=90)

    plt.show()

def drawCheckPicture():

    plt.figure(2)
    plt.xlabel('Time(h)')
    plt.ylabel('Number Of People')

    x = [i for i in range(24)]
    for each in range(3):
         plt.plot(x,variable.classCheckTime[each],label=NumToClass[each])

    plt.legend()
    plt.show()

if __name__ == '__main__':
    #statisticsClassFile()
    print "finish 1"
    statisticsClassCheck()
    print "finish 2"

    #drawFilePicture()
    drawCheckPicture()