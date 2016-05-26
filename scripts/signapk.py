#encoding:utf-8
import os, sys

#APK重新签名
def signAPK(apkFile, keyStoreFile, storePass, alianName, keyPass):
    signedFile = apkFile.replace('.apk', '_signed.apk')
    command = 'jarsigner -verbose -certs -digestalg SHA1 -sigalg MD5withRSA -sigfile CERT -keystore ' + keyStoreFile +' -storepass ' + storePass + ' -signedjar ' + signedFile + ' ' + apkFile +  ' ' + alianName + ' -keypass ' + keyPass
    os.system(command)
    os.system(os.getcwd() + '/tools/zipalign -v 4 '+ apkFile + ' ' + signedFile)
    os.remove(apkFile)
    os.rename(signedFile, apkFile)

if __name__ == '__main__':
	signAPK(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
