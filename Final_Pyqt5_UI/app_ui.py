# 필요한 모듈 import
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel, QPushButton, QMessageBox, \
    QDesktopWidget, QGridLayout, QTextBrowser, QVBoxLayout, QDialog, QScrollArea
import pandas as pd

# 전역변수1 : 각 년도별 <제목 -노래> 형식으로 저장
title_artist_1990 = []
title_artist_2000 = []
title_artist_2010 = []

# 전역변수2 : 각 년도별 <가수, 제목, 장르, 가사, 분위기 > 형식으로 저장
inform_1990 = []
inform_2000 = []
inform_2010 = []

# 전역변수3 : 현재 노래 정보
current_artist = ""
current_title = ""
current_genre = ""
current_release = ""
current_lyric = ""
current_thema = []
match = []

class SongData:
    def __init__(self, release, artist, title, genre, lyric, thema):
        self.release = release
        self.artist = artist
        self.title = title
        self.genre = genre
        self.lyric = lyric
        self.thema = thema

class App(QWidget):

    def __init__(self):
        super().__init__()
        #self.title = '팀 뉴트로 데모'
        #self.left = 100
        #self.top = 100
        #self.width = 300
        #self.height = 100
        self.initUI()

    def initUI(self):
        global current_artist
        global current_title
        global current_genre
        global current_release
        global current_lyric
        global match
        self.setWindowTitle('Team Newtro Demo') # 타이틀 바
        self.resize(400,300) # 위젯 너비,높이 설정
        self.center() # 위젯 뜨는 위치 가운데로 설정


        year = self.getYear() # 년도 선택
        song = self.getSong(year) # 노래 선택

        # items = ("1990년대 ", "2000년대 ", "2010년대 ")
        str1 = "선택한 노래는 <" + song + ">입니다 \n"

        store_current(song, year)

        str2 = "장르 :" + current_genre + " | 분위기 : " + str(current_thema) + "\n\n"
        str3 = "====비슷한 분위기의 노래를 찾아드립니다====\n"

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QLabel(str1),0, 0)
        grid.addWidget(QLabel(str2), 1, 0)
        grid.addWidget(QLabel(str3), 3, 0)

        btnRun1 = QPushButton("곡 상세 정보 ", self)  # 버튼 텍스트
        btnRun1.clicked.connect(self.btnRun_clicked1)  # 클릭 시 실행할 function
        grid.addWidget(btnRun1, 2, 0)

        btnRun2 = QPushButton("비슷한 노래 찾기", self)
        btnRun2.clicked.connect(self.btnRun_clicked2)
        grid.addWidget(btnRun2, 4, 0)

        self.dialog = QDialog()
        self.show()

    def btnRun_clicked1(self):
        global current_artist
        global current_title
        global current_genre
        global current_release
        global current_lyric
        global current_thema

        # add label
        artist_label = QLabel('가수 : ' + current_artist, self.dialog)
        artist_label.move(10,10)
        title_label = QLabel('노래 제목 : '+ current_title, self.dialog)
        title_label.move(10, 30)
        genre_label = QLabel('장르 : '+ current_genre, self.dialog)
        genre_label.move(10, 50)
        #thema_label = QLabel('분위기: '+ current_thema, self.dialog)
        #thema_label.move(10, 70)
        release_label = QLabel('발매년도 : ' + str(current_release), self.dialog)
        release_label.move(10, 70)
        temp = "================가사=================\n\n"
        lyric_label = QLabel(temp + add_newline(list(current_lyric)), self.dialog)
        lyric_label.move(10, 110)

        # 버튼 추가
        btnDialog = QPushButton("OK", self.dialog)
        btnDialog.move(200, 700)
        btnDialog.clicked.connect(self.dialog_close)

        # QDialog 세팅
        self.dialog.setWindowTitle('곡 상세 정보 ')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(300, 800)
        self.dialog.show()
        # Dialog 닫기 이벤트

    def dialog_close(self):
        self.dialog.close()

    def btnRun_clicked2(self):
        global current_title
        global current_thema
        global match

        #print(type(current_thema))

        year = self.getYear()
        tmp = current_thema.replace(",", "")
        tmp = tmp.replace("'", "")
        tmp = tmp.replace("[", "")
        tmp = tmp.replace("]", "")
        current_thema = tmp.split()

        if year == "1990년대 ":
            for i in range(1,len(inform_1990)-1):
                current_cnt = len(current_thema)
                match_cnt = 0
                for j in range(len(current_thema)):
                    if(current_thema[j] in inform_1990[i].thema):
                        #print(current_thema[j], ' ', inform_1990[i].thema)
                        match_cnt += 1
                #print(match_cnt)
                if( current_cnt == 1 and match_cnt == 1):
                    match.append(inform_1990[i])
                elif( match_cnt + current_cnt > current_cnt + 1 ):
                    print(current_thema, ' ', inform_1990[i].thema)
                    match.append(inform_1990[i])

        if year == "2000년대 ":
            for i in range(1,len(inform_2000)-1):
                current_cnt = len(current_thema)
                match_cnt = 0
                for j in range(len(current_thema)):
                    if(current_thema[j] in inform_2000[i].thema):
                        #print(current_thema[j], ' ', inform_1990[i].thema)
                        match_cnt += 1
                #print(match_cnt)
                if( current_cnt == 1 and match_cnt == 1):
                    match.append(inform_2000[i])
                elif( match_cnt + current_cnt > current_cnt + 1 ):
                    print(current_thema, ' ', inform_2000[i].thema)
                    match.append(inform_2000[i])

        if year == "1990년대 ":
            for i in range(1,len(inform_2010)-1):
                current_cnt = len(current_thema)
                match_cnt = 0
                for j in range(len(current_thema)):
                    if(current_thema[j] in inform_2010[i].thema):
                        #print(current_thema[j], ' ', inform_1990[i].thema)
                        match_cnt += 1
                #print(match_cnt)
                if( current_cnt == 1 and match_cnt == 1):
                    match.append(inform_2010[i])
                elif( match_cnt + current_cnt > current_cnt + 1 ):
                    print(current_thema, ' ', inform_2010[i].thema)
                    match.append(inform_2010[i])

        self.getRecommendSong()
        print(match)
        #elif year == "2000년대 ":
        #else:


    def getYear(self):
        items = ("1990년대 ", "2000년대 ", "2010년대 ")
        item, okPressed = QInputDialog.getItem(self, "팀 뉴트로 데모", "시대 선택(1990~2020) ", items, 0, False)
        return item

    def getRecommendSong(self):
        global match
        tmp = ""

        for i in range(len(match)):
            tmp += '<'+ match[i].title + '> '
            tmp += '-'+ match[i].artist + ' '
            tmp += match[i].thema
            tmp += '\n'
            if( i > 10 ):
                break

        recommend = QLabel(tmp, self.dialog)
        recommend.move(10,10)
        # QDialog 세팅
        self.dialog.setWindowTitle('비슷한 분위기 곡 추천  ')
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(500, 300)
        self.dialog.show()

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




    def show_inform(self):
        QMessageBox.about(self, "message", "clicked")

    def center(self): # 창을 화면의 가운데로 띄우는 함수
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def store_current(song, year):
    global current_artist
    global current_title
    global current_genre
    global current_release
    global current_lyric
    global current_thema

    if year == "1990년대 ":
        i = title_artist_1990.index(song)
        current_artist = inform_1990[i].artist
        current_title = inform_1990[i].title
        current_genre = inform_1990[i].genre
        current_release = inform_1990[i].release
        current_lyric = inform_1990[i].lyric
        current_thema = inform_1990[i].thema
    elif year == "2000년대 ":
        i = title_artist_2000.index(song)
        current_artist = inform_2000[i].artist
        current_title = inform_2000[i].title
        current_genre = inform_2000[i].genre
        current_release = inform_2000[i].release
        current_lyric = inform_2000[i].lyric
        current_thema = inform_2000[i].thema
    else:
        i = title_artist_2010.index(song)
        current_artist = inform_2010[i].artist
        current_title = inform_2010[i].title
        current_genre = inform_2010[i].genre
        current_release = inform_2010[i].release
        current_lyric = inform_2010[i].lyric
        current_thema = inform_2010[i].thema


def add_newline(lyrics):
    cnt = 0
    for i in range(len(lyrics)):
        if lyrics[i] == ' ':
            cnt += 1
        if cnt > 5 and lyrics[i] == ' ':
            cnt = 0
            lyrics[i] = '\n'
    return ''.join(lyrics)

def tsv_to_list():
    list_1990 = pd.read_csv('1990s.tsv', sep='\t', encoding='utf-8')
    list_2000 = pd.read_csv('2000s.tsv', sep='\t', encoding='utf-8')
    list_2010 = pd.read_csv('2010s.tsv', sep='\t', encoding='utf-8')

    #print(list_1990.columns)
    for i in range(len(list_1990)):
        inform_1990.append(SongData(list_1990['release'][i], list_1990['artist'][i],list_1990['title'][i],list_1990['genre'][i], list_1990['lyric'][i],list_1990['thema'][i]))
        tmp = list_1990['title'][i]
        tmp += " -"
        tmp += list_1990['artist'][i]
        title_artist_1990.append(tmp)

    #print(list_2000.columns)
    for i in range(len(list_2000)):
        inform_2000.append(SongData(list_2000['release'][i], list_2000['artist'][i],list_2000['title'][i],list_2000['genre'][i], list_2000['lyric'][i], list_2000['thema'][i]))
        tmp = list_2000['title'][i]
        tmp += " -"
        tmp += list_2000['artist'][i]
        title_artist_2000.append(tmp)

    #print(list_2010.columns)
    for i in range(len(list_2010)):
        inform_2010.append(SongData(list_2010['release'][i],list_2010['artist'][i],list_2010['title'][i],list_2010['genre'][i], list_2010['lyric'][i], list_2010['thema'][i]))
        tmp = list_2010['title'][i]
        tmp += " -"
        tmp += list_2010['artist'][i]
        title_artist_2010.append(tmp)



if __name__ == '__main__':
    tsv_to_list()
    app = QApplication(sys.argv) # UI 객체 생성
    ex = App()
    sys.exit(app.exec_())