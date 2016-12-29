#!/usr/bin/env python
# encoding:utf-8
import requests
import sys
from bs4 import BeautifulSoup


# define-start
url = "http://dict.cn/"
# define-end


def getBaseMeaning(soup):
    '''
    获取单词的基本含义
    '''
    meanings = []
    dict_base_ul = soup.find("ul", class_="dict-basic-ul")
    lis = dict_base_ul.findAll("li")
    lis = lis[0:-1]  # 去掉最后的<script>
    for li in lis:
        meaning = {}
        meaning['part_of_speech'] = ""
        # 有时候会存在一个词没有词性这个标签 ,这里主要解决这个问题 , 当没有标签的时候 , 就直接赋值为空字符串
        try:
            spans = li.findAll("span")
            for span in spans:
                meaning['part_of_speech'] = span.text
            strongs = li.findAll("strong")
        except:
            pass
        for strong in strongs:
            meaning['meaning'] = strong.text
        meanings.append(meaning)
    return meanings


def initUserInput():
    if len(sys.argv) != 2:
        print "Usage : python " + sys.argv[0] + " [word]"
        print "Example : python " + sys.argv[0] + " \"help\""
        exit(1)


def main():
    initUserInput()
    word = sys.argv[1]
    content = requests.get(url + word).text.encode("UTF-8")
    soup = BeautifulSoup(content, "html.parser")
    meanings = getBaseMeaning(soup)
    for meaning in meanings:
        part_of_speech = meaning['part_of_speech']
        meaning = meaning['meaning']
        print part_of_speech + "\t" + meaning


if __name__ == "__main__":
    main()
