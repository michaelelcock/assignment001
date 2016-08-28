from bs4 import BeautifulSoup
import requests
import csv
import pickle
import sys
from sys import stdin
import shelve


class Scrapper(object):

    @staticmethod
    def web_scrapper():
        data = []

        r = requests.get('https://en.wikipedia.org/wiki/List_of_Magic:_The_Gathering_sets').text

        soup = BeautifulSoup(r, 'html.parser')

        table = soup.find('table', attrs={'class': 'wikitable'})

        rows = table.find_all('tr')

        for row in rows[:10]:
            cols = row.find_all(['td', 'th'])
            data.append([col.text for col in cols])
        return data


# for pack in data:
# print(pack)

    @staticmethod
    def get_pack_name():
        print("What Pack where you looking for?")

        pack_name = stdin.readline()
        return pack_name

    @staticmethod
    def pickle_file():
        output = open("scrapping.pkl", "wb")
        pickle.dump(data, output)
        output.close()

    @staticmethod
    def get_pickle_file():
        input_file = open("scrapping.pkl", "rb")
        data1 = pickle.load(input_file)
        inputFile.close()
        print(data1)
        