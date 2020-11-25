import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

title_artist_1990 = []
title_artist_2000 = []
title_artist_2010 = []

inform_1990 = []
inform_2000 = []
inform_2010 = []

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = '팀 뉴트로 데모'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        year = self.getYear() # 년도 선택
        song = self.getSong(year) # 노래 선택
        self.showChoice(year, song)
        #self.MappingYear() # 매핑 년도 선택
        #self.getRecommandList() # 추천 노래 리스트

        self.show()

    def getYear(self):
        items = ("1990년대 ", "2000년대 ", "2010년대 ")
        item, okPressed = QInputDialog.getItem(self, "팀 뉴트로 데모", "시대 선택(1990~2020) ", items, 0, False)
        return item

    def getSong(self, year):
        if year == "1990년대 ":
            items = title_artist_1990
            item, okPressed = QInputDialog.getItem(self, "팀 뉴트로 데모", "노래 선택 ", items, 0, False)
            return item
        elif year == "2000년대 ":
            items = title_artist_2000
            item, okPressed = QInputDialog.getItem(self, "팀 뉴트로 데모", "노래 선택 ", items, 0, False)
            return item
        else :
            items = title_artist_2010
            item, okPressed = QInputDialog.getItem(self, "팀 뉴트로 데모", "노래 선텍 ", items, 0, False)
            return item


    def showChoice(self, year, song):
        items = ("1990년대 ", "2000년대 ", "2010년대 ")
        str1 = "선택한 노래는 <" + song + ">입니다 \n"
        if year == "1990년대 ":
            i = title_artist_1990.index(song)
            genre = inform_1990[i].genre
        elif year == "2000년대 ":
            i = title_artist_2000.index(song)
            genre = inform_2000[i].genre
        else:
            i = title_artist_2010.index(song)
            genre = inform_2010[i].genre

        str2 = "장르 :" + genre + " | 분위기 : 이별, 잔잔한 \n\n"
        str3 = "====비슷한 분위기의 노래를 찾아드립니다====\n"
        str4 = "매핑 년도 \n"
        str = str1 + str2 + str3 + str4
        item, okPressed = QInputDialog.getItem(self, "팀 뉴트로 데모",str, items, 0, False)
        return item

def tsv_to_list():
    list_1990 = pd.read_csv('1990s.tsv', sep='\t', encoding='utf-8')
    list_2000 = pd.read_csv('2000s.tsv', sep='\t', encoding='utf-8')
    list_2010 = pd.read_csv('2010s.tsv', sep='\t', encoding='utf-8')

    #print(list_1990.columns)
    for i in range(len(list_1990)):
        inform_1990.append(SongData(list_1990['artist'][i],list_1990['title'][i],list_1990['genre'][i]))
        tmp = list_1990['title'][i]
        tmp += " -"
        tmp += list_1990['artist'][i]
        title_artist_1990.append(tmp)

    #print(list_2000.columns)
    for i in range(len(list_2000)):
        inform_2000.append(SongData(list_2000['artist'][i],list_2000['title'][i],list_2000['genre'][i]))
        tmp = list_2000['title'][i]
        tmp += " -"
        tmp += list_2000['artist'][i]
        title_artist_2000.append(tmp)

    #print(list_2010.columns)
    for i in range(len(list_2010)):
        inform_2010.append(SongData(list_2010['artist'][i],list_2010['title'][i],list_2010['genre'][i]))
        tmp = list_2010['title'][i]
        tmp += " -"
        tmp += list_2010['artist'][i]
        title_artist_2010.append(tmp)

class SongData:
    def __init__(self, artist, title, genre):
        self.artist = artist
        self.title = title
        self.genre = genre

if __name__ == '__main__':
    tsv_to_list()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())