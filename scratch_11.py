#每隔3秒打印一个随机变量，共计30秒
#这是测试
import random,time
timeLit=[]
for i in range(3):
    print(random.random())
    NowTime=time.asctime(time.localtime(time.time()))#获取时间
    timeLit.append(NowTime)#将获取的时间写入列表
    time.sleep(3)
    print(timeLit)

#将时间列表写入samplelist文本文件
with open("sampleList.txt","a") as fileObject: # r 只读，w 只写,清空原内容，x 只写，存在即报错， a 追加，存在可追加
   for ip in timeLit:
       fileObject.write(ip)
       fileObject.write('\n') #逐个换行写入
