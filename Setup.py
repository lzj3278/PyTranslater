#!/usr/bin/env python
# encoding:utf8

import os
import shutil
import ConfigParser


# global-start
configParser = ConfigParser.SafeConfigParser()
installPath = "/opt/fy/"
# global-end


def getConfigParser():
    global configParser
    configParser.read("./Config/config.conf")
    return configParser


def copyFile(src, dst):
    srcFile = open(src, "r")
    dstFile = open(dst, "w")
    for line in srcFile:
        dstFile.write(line)
    dstFile.close()
    srcFile.close()


def chooseYoudaoAPI(configParser):
    # 让用户配置自己申请的有道翻译的key和keyfrom
    print "请对有道翻译模块进行必要的配置 , 如果您还没有申请您的key和keyfrom"
    print "您可以访问 : http://fanyi.youdao.com/openapi?path=data-mode 进行获取"
    key = raw_input("请输入您在有道翻译API平台申请得到的key : ")
    keyfrom = raw_input("请输入您在有道翻译API平台申请时填写的应用名称(keyfrom) : ")
    configParser.set("YoudaoAPI", "key", key)
    configParser.set("YoudaoAPI", "keyfrom", keyfrom)
    configParser.write(open("./Config/config.conf", "w"))
    print "配置写入成功!"


def chooseSpider():
    print "基于爬虫的翻译脚本不需要进行key或者appid的配置"
    print "配置写入成功!"


def chooseBaiduAPI(configParser):
    # 让用户配置自己申请的有道翻译的key和appid
    print "请对百度翻译模块进行必要的配置 , 如果您还没有申请您的key和keyfrom"
    print "您可以访问 : http://api.fanyi.baidu.com/api/trans/product/index 进行获取"
    appid = raw_input("请输入您在百度翻译API平台申请得到的appid : ")
    key = raw_input("请输入您在百度翻译API平台申请时得到的key : ")
    configParser.set("BaiduAPI", "appid", appid)
    configParser.set("BaiduAPI", "key", key)
    configParser.write(open("./Config/config.conf", "w"))
    print "配置写入成功!"


def showModules():
    print "模块列表 : "
    print "\t1. YoudaoAPI"
    print "\t2. Spider"
    print "\t3. BaiduAPI"


def chooseModule():
    moduleNumber = raw_input("请输入您需要选择使用的模块序号 : ")
    moduleNumber = int(moduleNumber)
    if moduleNumber == 1:
        chooseYoudaoAPI(configParser)
    elif moduleNumber == 2:
        chooseSpider()
    elif moduleNumber == 3:
        chooseBaiduAPI(configParser)


def showSuccess():
    print "安装完成 , 请输入 : 'fy help' 进行测试"


def showHelp():
    print "请您以管理员的身份运行 , 如果您并没有这样做 , 安装可能会失败"
    print "如果您确保您已经以管理员的身份运行了该脚本 , 请您输入 y 以继续安装"
    print "如果您并不确定 , 请您输入 n 结束脚本 , 然后使用sudo以管理员的身份运行"
    choice = ""
    while choice == "":
        choice = raw_input("请选择 : ")
        if choice.startswith('y') or choice.startswith('Y'):
            return True


def getCurrentDicName():
    temp = os.getcwd()
    return temp.split("/")[-1]

def main():
    if not showHelp():
        exit(1)
    global configParser
    copyFile("./Config/config.example.conf", "./Config/config.conf")
    configParser = getConfigParser()
    showModules()
    chooseModule()
    # 先删除之前的安装
    os.system("sudo rm -rf /opt/fy/")
    os.system("sudo rm /bin/fy")
    # 开始安装
    os.system("pip install -r requirements.txt")
    currentDicName = getCurrentDicName()
    shutil.copytree("../" + currentDicName, installPath)
    # create a soft link
    os.system("ln -s " + installPath + "fy" + " /bin/fy")
    showSuccess()


if __name__ == '__main__':
    main()
