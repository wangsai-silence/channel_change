# 目录说明

 - channels 用于存放新渠道列表文件
 - keystores 用于存放签名文件
 - scripts 所有相关的Python脚本
 - tools  打包用到的所有工具包
 - run.bat 脚本入口文件

-----
 # 参数说明
 - apkFile 源apk
 - keyStoreFile 签名文件
 - storePass 签名文件密码
 - alianName 签名别名
 - keyPass 签名密码
 - old_channel 源apk中的渠道字符串
 - newChannelFile 新渠道列表对应的文件（从文件中读取新渠道列表）
 - prefix 生成新的apk过程中，添加的前缀，主要是用于区分不同的apk包

#环境说明
　　Windows Python2.7
　　    `Linux环境下需要替换tools内相关的tool，从android tools文件夹下查找即可；`
　　    
-----

#使用方法

 1. 将新的渠道列表添加到channels文件夹内
 2. 添加源apk文件
 3. 修改run.bat内的相关参数，依据参数说明
 4. 点击run.bat运行程序

 