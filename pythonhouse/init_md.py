# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests

def rootsoup(link,target):
    '''
    指定某个链接的网页，返回网页中class 为target 的div标签(结构化形态)
    '''
    fo = open(link,"r+",encoding='UTF-8')
    line = fo.readline()
    content = ''
    while line:
        content = content + line
        line = fo.readline()
    fo.close()
    soup_content = BeautifulSoup(content,"lxml")
    target_content = soup_content.find("div",target)
    return target_content

def output_md(titles,location):
    '''
    将列表输出为markdown形式的无序列表，存放于content子目录内
    '''
    mdfile = open(location,"w+",encoding='UTF-8')
    try:
        for index in range(len(titles)-1):
            mdfile.write("- ["+titles[index]+"](https://stata-club.github.io/library/pythonhouse/content/"+titles[index]+".html)\n")
    finally:
        mdfile.close()
        return 1
    
def init_html(title,link):
    '''
    给定网页链接，和相应名称，保存为本地html网页
    '''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent': user_agent}
    r = requests.get(link,headers=headers)
    try:
        html_content = open(title+".html","w+",encoding = 'UTF-8')
        html_content.write(r.text)
        html_content.close()
    finally:
        return 1
    
conta = rootsoup("index.html","rich_media_content")
'''
找到conta标签下所有的超链接及题目列表
'''

title = []
for tag in conta.find_all('a'):
    #init_html(tag.next_element,tag.get('href'))
    while(isinstance(tag.next_element,NavigableString) == False):
        tag = tag.next_element
    title.append(tag.next_element)
    print(title[-1])
print(len(title)-1)
ans = output_md(title,"list.md")
    
