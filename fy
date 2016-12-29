#!/usr/bin/env python
# encoding:utf8
from __future__ import print_function
import os
import sys

if sys.version_info[0] < 3:
    from ConfigParser import SafeConfigParser
else:
    from configparser import ConfigParser as SafeConfigParser


def get_config():
    configParser = SafeConfigParser()
    configParser.read("/opt/fy/Config/config.conf")
    defaultModule = configParser.get("Global", "defaultModule")
    return (configParser, defaultModule)


def printHelp():
    binName = sys.argv[0].split("/")[-1]
    print("Usage : ")
    print("\t {binName} [word]".format(binName=binName))
    print("Example : ")
    print("\t {binName} help".format(binName=binName))
    print("\t {binName} 帮助".format(binName=binName))
    print("\t {binName} \"help me\"".format(binName=binName))


def getUserInput():
    if len(sys.argv) != 2:
        printHelp()
        exit(1)
    else:
        return sys.argv[1]


def checkConfig(configParser, ModuleName):
    if ModuleName == "YoudaoAPI":
        key = configParser.get("YoudaoAPI", "key")
        keyfrom = configParser.get("YoudaoAPI", "keyfrom")
        if key == "":
            print("Please config your key!")
            print("You can use Setup.py as a install guide")
            return False
        if keyfrom == "":
            print("Please config your keyfrom!")
            print("You can use Setup.py as a install guide")
            return False
        return True
    elif ModuleName == "BaiduAPI":
        key = configParser.get("BaiduAPI", "key")
        appid = configParser.get("BaiduAPI", "appid")
        if key == "":
            print("Please config your key!")
            print("You can use Setup.py as a install guide")
            return False
        if appid == "":
            print("Please config your appid!",)
            print("You can use Setup.py as a install guide")
            return False
        return True
    elif ModuleName == "Spider":
        return True
    else:
        return False


def main():
    configParser, defaultModule = get_config()
    checkConfig(configParser, defaultModule)
    word = getUserInput()
    command = 'python /opt/fy/Modules/{defaultModule}.py' \
              ' \" {word} \"'.format(defaultModule=defaultModule,
                                     word=word)
    os.system(command)


if __name__ == '__main__':
    main()
