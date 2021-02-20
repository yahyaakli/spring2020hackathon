import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os.path
from os import path

class Recyable():
    def __init__(self):
        self.__recycable_items = self.read_items()

    def getRecycleDict(self):
        return self.__recycable_items

    def getRecycables(self):
        return self.__recycable_items.keys()

    def getRecycableInfo(self,item):
        return self.__recycable_items[item]['content']

    def showRecycableInfo(self,item):
        for phrase in self.__recycable_items[item]['content']:
            print(phrase[:-1])

    def read_items(self):
        if(path.exists('../uploads/data.json')):
            print("reading data from json file")
            with open('../uploads/data.json', 'r') as fp:
                items_dict = json.load(fp)
        else:
            print("generating json data file")
            url = "https://solar.world.org/weo/recycle"
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html5lib')

            #extract recycble items
            items = soup.find_all('a')
            items_dict = {}
            element_count = 0
            for item in items:
                if 'http' not in item.get('href'):
                    items_dict[item.string] = {'href':item.get('href')}
                    element_count+=1


            #extract information about the items
            element_scrapped = 0
            for links,key in zip(items_dict.values(),items_dict.keys()):
                url = "https://solar.world.org"+links['href'][2:]
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html5lib')
                scrapped = soup.find_all('li')
                for scrap in scrapped:
                    if 'content' not in items_dict[key]:
                        items_dict[key]['content'] = [scrap.string]
                    else:
                        items_dict[key]['content'].append(scrap.string)
                element_scrapped+=1
                print("element scanned "+str(element_scrapped)+" out of "+str(element_count))

            with open('../uploads/data.json', 'w') as fp:
                json.dump(items_dict, fp)
        return items_dict

R = Recyable()
R.showRecycableInfo('Umbrella')