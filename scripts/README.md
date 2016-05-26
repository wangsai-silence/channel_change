readme

标签（空格分隔）： 未分类

---




# 文件说明：
　　channels  //用于存放新渠道相关文件，每个文件中是新渠道的集合
　　keystores //用于存放签名文件
　　scripts //打包相关脚本
　　tools //打包所需的相关工具
　　run.bat //脚本入口 `使用前需要修改此文件内的参数`

#参数说明
　　apkFile //源apk文件
　　keyStoreFile //签名文件
　　storePass 签名文件的密码
　　alianName 具体签名
　　keyPass  签名密码
　　old_channel  源文件中的渠道字符串
　　newChannelFile 新渠道列表文件
　　prefix = 生成的新apk名称加前缀

# 使用方法： 

- 环境 Windows Python 2.7（Linux下需要替换tools中相应的工具，从Android的相应工具包中拿出来，自行替换）

- 将新的渠道列表统一放置到channels文件夹下，供批量打包用

- 在run.bat 为脚本入口，执行前修改内部相应参数
