import pymongo
import matplotlib.pyplot as plt

client = pymongo.MongoClient("localhost",27017)
db = client.test

FileToNum = {'voice':0, 'image':1, 'video':2, 'shortvideo':3}
ClassToNum = {'TANSLATE_CLAZZ':0, 'ENGLISH_CLAZZ':1, 'GRE_CLAZZ':2}
NumToClass = {0:'TANSLATE_CLAZZ', 1:'ENGLISH_CLAZZ', 2:'GRE_CLAZZ'}

cols = 4
rows = 3
classFileNum = [[0 for col in range(cols)]for row in range(rows)]
cols = 24
rows = 3
classCheckTime = [[0 for col in range(cols)]for row in range(rows)]

lostNum = 0

def statisticsClassFileType(id,fileType):
    global lostNum
    global classFileNum

    collect = db.AccountCard
    data = collect.find_one({'openId':id})
    if data:
        clazzKey = data['clazzKey'].encode('utf-8')
        classFileNum[ClassToNum[clazzKey]][FileToNum[fileType]] += 1
    else:
        lostNum += 1

def statisticsClassCheckTime(id,hour):
    global lostNum
    global classCheckTime

    collect = db.AccountCard
    data = collect.find_one({'openId':id})
    if data:
        clazzKey = data['clazzKey'].encode('utf-8')
        classCheckTime[ClassToNum[clazzKey]][hour] += 1
    else:
        lostNum += 1


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
    global classFileNum
    ax1 = plt.subplot(131)
    ax2 = plt.subplot(132)
    ax3 = plt.subplot(133)

    labels = ['voice', 'image', 'video', 'shortvideo']

    plt.sca(ax1)
    plt.pie(classFileNum[0], labels=labels, labeldistance=1.1, autopct='%3.1f%%', startangle=90)
    plt.sca(ax2)
    plt.pie(classFileNum[1], labels=labels, labeldistance=1.1, autopct='%3.1f%%', startangle=90)
    plt.sca(ax3)
    plt.pie(classFileNum[2], labels=labels, labeldistance=1.1, autopct='%3.1f%%', startangle=90)

    plt.show()

def drawCheckPicture():
    global classCheckTime

    plt.xlabel('Time(h)')
    plt.ylabel('Number Of People')

    x = [i for i in range(24)]
    for each in range(3):
         plt.plot(x,classCheckTime[each],label=NumToClass[each])

    plt.legend()
    plt.show()

if __name__ == '__main__':
    #statisticsClassFile()
    print "finish 1"
    statisticsClassCheck()
    print "finish 2"

    #drawFilePicture()
    drawCheckPicture()