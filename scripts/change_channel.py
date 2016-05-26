#encoding:utf-8
import zipfile, shutil, sys, array, os, signapk, axmlparser, time

xmlFile = 'AndroidManifest.xml'
#格式化字符串
def formatStr(str):
    return str.strip().lstrip().rstrip(',')

#删除压缩文件中的指定文件或文件夹
def deleteMETAFiles(destApk):
    zipf = zipfile.ZipFile(destApk, 'a')
    namelist = zipf.namelist()
    zipf.close()

    for meta in namelist:
        if 'META-INF/' in meta:
            cmd = os.getcwd() + '/tools/aapt r ' + destApk + ' ' + meta
            os.system(cmd)
            print(cmd)

#获取当前时间
def getCurTime():
    return time.strftime('%m%d%H%M%S', time.localtime(time.time()))

if __name__ == '__main__':
    apkFile = sys.argv[1]
    keyStoreFile = sys.argv[2]
    storePass = sys.argv[3]
    alianName = sys.argv[4]
    keyPass = sys.argv[5]
    old_channel = sys.argv[6]
    newChannelFile = sys.argv[7]
    prefix = sys.argv[8]

    #创建文件夹
    outputDirName = prefix + 'output_' + getCurTime()
    if not os.path.exists(outputDirName):
        os.makedirs(outputDirName)

    #读取渠道列表
    channel_list = []
    for channel in open(newChannelFile):

        channel_list.append(format(channel))
        destApk = outputDirName + '/' + prefix + formatStr(channel) + '.apk'
        
        #复制apk，重命名
        shutil.copyfile(apkFile, destApk)
                        
        #解压apk,得到xml        
        zipped = zipfile.ZipFile(destApk, 'r')
        zipped.extract(xmlFile)
        zipped.close()

        #读取二进制数据
        axml_array = bytearray(os.path.getsize(xmlFile))
        with open(xmlFile, 'rb') as tmp:
            tmp.readinto(axml_array)
        
        #修改数据
        axmlparser.replace_axml_string(axml_array, old_channel, formatStr(channel))
        
        #回写到xml文件
        tmp = open(xmlFile, 'wb')
        tmp.write(axml_array)
        tmp.close()
        

        print(os.path.abspath('.'))
        #压缩回apk 先删除原来的，然后将现在的添加进去
        cmd = os.getcwd() + '/tools/aapt r ' + destApk + ' ' + xmlFile
        os.system(cmd)
        os.system(os.getcwd() + '/tools/aapt a ' + destApk + ' ' + xmlFile)
        
        #删除META中的各种加密验证文件
        deleteMETAFiles(destApk)
              

        #重新签名文件
        signapk.signAPK(destApk, keyStoreFile, storePass, alianName, keyPass)

        
        
