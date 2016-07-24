#-*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.proxy import *
service_args = [
 '--proxy=localhost',
 '--proxy-type=socks5',
 ]
driver=webdriver.PhantomJS(service_args=service_args)

def getData():
    categorylist=['ANDROID_WEAR',
                  'BOOKS_AND_REFERENCE',
                  'BUSINESS',
                  'COMICS',
                  'COMMUNICATION',
                  'EDUCATION',
                  'ENTERTAINMENT',
                  'FINANCE',
                  'HEALTH_AND_FITNESS',
                  'LIBRARIES_AND_DEMO',
                  'LIFESTYLE',
                  'MEDIA_AND_ViDEO',
                  'MEDICAL',
                  'MUSIC_AND_AUDIO',
                  'NEWS_AND_MAGAZINES',
                  'PERSONALIZATION',
                  'PHOTOGRAPHY',
                  'PRODUCTIVITY',
                  'SHOPPING',
                  'SOCIAL',
                  'SPORTS',
                  'TOOLS',
                  'TRANSPORTATION',
                  'TRAVEL_AND_LOCAL',
                  'WEATHER',
                  'GAME_ACTION',
                  'GAME_ADVENTURE',
                  'GAME_ARCADE',
                  'GAME_BOARD',
                  'GAME_CARD',
                  'GAME_CASINO',
                  'GAME_CASUAL',
                  'GAME_EDUCATIONAL',
                  'GAME_MUSICAL',
                  'GAME_PUZZLE',
                  'GAME_RACING',
                  'GAME_ROLE_PLAYING',
                  'GAME_SIMULATION',
                  'GAME_SPORTS',
                  'GAME_STRATEGY',
                  'GAME_WORD',
                  'GAME_TRIVIA'
                  ]
    for category in categorylist:
        url="https://play.google.com/store/apps/category/"+category
        driver.get(str(url))
        driver.maximize_window()
        time.sleep(1)
        collections=driver.find_elements_by_xpath("//a[contains(@href, 'collection')]")
        for collection in collections:
            print category+','+collection.text+','+collection.get_attribute('href')
    return 0

def getUrl(url):
    urllist=[]
    f=file(url,"r+")
    lines=f.readlines()
    for line in lines:
        l=line.strip('\n').split(',')
        urllist.append([l[0],l[1]])
    return urllist

def getResult(alllist):
    for result in alllist:
        f=file('result.txt','a')
        f.write(result[0]+','+result[1]+'\n')
    return 0

def getPkg(urllist):
    alllist=[]
    for keyurl in urllist:
        title=keyurl[0]
        url=keyurl[1]
        driver.get(str(url))
        driver.maximize_window()
        time.sleep(3)
        pkgs = driver.find_elements_by_xpath("//a[contains(@href, 'details')]")
        pkglist=getAll(pkgs)
        for pkg in pkglist:
            alllist.append([title,pkg])
    return alllist

def getAll(pkgs):
    linklist = []
    for url in pkgs:
        if url.get_attribute("href") not in linklist:
            linklist.append(url.get_attribute("href"))
    return linklist

urllist=getUrl('data.txt')
alllist=getPkg(urllist)
getResult(alllist)
driver.close()
