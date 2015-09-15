#encoding:utf-8
import zipfile, shutil, sys, array, os, signapk, axmlparser, datetime

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
            cmd = 'aapt r ' + destApk + ' ' + meta
            os.system(cmd)
            print(cmd)

'''
python parseAxml.py yourApkFile yourStoreFile yourStorePasswd yourAlian youAlianPasswd oldChannelStr
'''
if __name__ == '__main__':
    apkFile = sys.argv[1]
    keyStoreFile = sys.argv[2]
    storePass = sys.argv[3]
    alianName = sys.argv[4]
    keyPass = sys.argv[5]
    old_channel = sys.argv[6]

    #读取渠道列表
    channel_list = []
    for channel in open('channels.txt'):
        t1 = datetime.datetime.now()
        
        channel_list.append(format(channel))
        destApk = 'output/' + formatStr(channel) + '.apk'
        
        #复制apk，重命名
        shutil.copyfile(apkFile, destApk)
        
        print('copy apk:' + bytes(datetime.datetime.now() - t1))
        
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
        
        print('alert xml:' + bytes(datetime.datetime.now() - t1))

        #压缩回apk 先删除原来的，然后将现在的添加进去
        cmd = 'aapt r ' + destApk + ' ' + xmlFile
        os.system(cmd)
        print(cmd)
        os.system('aapt a ' + destApk + ' ' + xmlFile)
        
        #删除META中的各种加密验证文件
        deleteMETAFiles(destApk)
        print('delete meta-inf:' + bytes(datetime.datetime.now() - t1))
        

        #重新签名文件
        signapk.signAPK(destApk, keyStoreFile, storePass, alianName, keyPass)
        print('sign apk:' + bytes(datetime.datetime.now() - t1))
        
        
        
