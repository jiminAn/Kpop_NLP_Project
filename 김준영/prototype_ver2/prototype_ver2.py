import sys
import numpy as np
import pandas as pd
import random
import gensim
from gensim import corpora


path = 'C:\\Users\\준영\\Desktop\\OneDrive - SangMyung University\\새 폴더\\ai\\자연어처리\\프로젝트\\프로토타입\\'
data = pd.read_csv(path + 'LDA_thema.tsv', sep='\t', encoding='utf-8')

ldamodel = gensim.models.LdaModel.load(path + '\\model.h5', mmap='r')

lyrics = []
for i in range(0,len(data)):
    lyrics.append(data.loc[i].loc['가사'].replace("\'", "").replace(" ", "").replace("[", "").replace("]", "").split(","))
data['가사'] = lyrics

dictionary = gensim.corpora.Dictionary.load(path + '\\lda_dict')


def print_select_list():
    print("시대를 입력하세요(1990~2020):")
    year = int(input())
    print('-----목록-----')

    #입력 받은 년대의 노래목록만 남김
    year = year * 10000
    print_data = data[data['년도'] >= year]
    print_data = print_data[print_data['년도'] < year + 100000]
    print_data = print_data.reset_index(drop=True)
    index_list = []
    
    #랜덤하게 3곡 프린트
    for i in range(0,3):
        j = random.randrange(0, len(print_data))
        index_list.append(j)
        print(i + 1, '.', print_data.loc[j].loc['제목'], '--', print_data.loc[j].loc['가수'])
    print('다음 중 한곡을 선택하세요:')
    n = int(input()) - 1
   
    topics= ldamodel.get_document_topics(dictionary.doc2bow(print_data.loc[index_list[n]].loc['가사']))
    prob_topic=[]
    #선택한 노래가 속할 토픽 중 가장 확률이 높은 토픽 선택
    for k in range(len(topics)):
        prob_topic.append(topics[k][1])
    topic=topics[prob_topic.index(max(prob_topic))][0]
    singer = print_data.loc[index_list[n]].loc['가수']
    title = print_data.loc[index_list[n]].loc['제목']
    genre = print_data.loc[index_list[n]].loc['장르']
    print("선택한 노래는 {} -- {} ({}) 입니다.".format(title,singer,genre))
    print("분위기:",print_data.loc[index_list[n]].loc['분위기'])
    print("======================================")
    return topic, singer, title


def recommend(topic, singer, title):
    print("매핑 년도는?:")
    year = int(input())
    print("선택 년도:{}년대".format(year))

    #매핑할 년도만 남김
    year = year * 10000
    rcmd_data = data[data['년도'] >= year]
    rcmd_data = rcmd_data[rcmd_data['년도'] < year + 100000]
    rcmd_data = rcmd_data.reset_index(drop=True)

    #입력받은 토픽과 같은 토픽에 속하는 노래 목록만 남
    for i in range(0,len(rcmd_data)):
        try:
            #토픽에 속할 확률이 0.5 이상인 토픽 선택
            topics = ldamodel.get_document_topics(dictionary.doc2bow(rcmd_data.loc[i].loc['가사']),0.5)[0][0]
        except:
            topics = -1
        if topics != topic:
            rcmd_data = rcmd_data.drop(i)
    rcmd_data = rcmd_data.reset_index(drop=True)

    print("   ====<{}--{} >와 비슷한 노래====  ".format(title, singer))
    for j in range(4):
        num = random.randrange(0, len(rcmd_data))
        print("list{}: {} -- {}".format(j + 1, rcmd_data.loc[num].loc['제목'], rcmd_data.loc[num].loc['가수']),rcmd_data.loc[num].loc['분위기'])
    

def main():
    while True:
        topic, singer, title = print_select_list()
        recommend(topic, singer, title)
        print("다시 하기 :1 --- 프로그램 종료 : 0")
        n=int(input())
        if n==0:
            sys.exit()
        elif n==1:
            continue
        else:
            print("잘못된 입력")
            sys.exit()
            

if __name__ == "__main__":
    main()
