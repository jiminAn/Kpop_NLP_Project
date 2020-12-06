# Introduction

## 2020-Fall-Semester NLP : Team Project

- 1992~2020년도 K-pop 아이돌 발매곡 데이터 셋을 이용한 NLP
- 팀 주제 : 특정 시대의 노래를 타깃으로 비슷한 분위기의 다른 세대 노래를 추천해주는 프로그램

# Team Member

## 팀 뉴트로

| 팀원                                                | 역할                     | 책임                                          |
| --------------------------------------------------- | ------------------------ | --------------------------------------------- |
| [jiminAn(안지민)](https://github.com/jiminAn)       | 팀장, 모델 설계, UI 개발 | LDA 모델 초기 설계 및 pyqt5을 이용한 UI디자인 |
| [201810794(이은후)](https://github.com/201810794)   | 모델 설계                | K-means초기 설계 & LDA 모델 최종 설계         |
| [kky0426(김준영)](https://github.com/kky0426)       | 데이터 전처리, 모델 설계 | 가사 전처리 및 LDA 모델 최종 설계             |
| [lee1996-ui(이선우)](https://github.com/lee1996-ui) | 문서관리                 | 프로젝트 최종 발표 및 ppt제작                 |



## LDA 모델을 적용한 <비슷한 분위기의 다른 세대 노래 추천 프로그램>

### 기술시연 영상
[![팀뉴트로 : 프로젝트 제안 발표](https://img.youtube.com/vi/8k6KAMpu6sM/0.jpg)](https://www.youtube.com/watch?v=8k6KAMpu6sM)

### 기능1. 년도별 노래 선택 -> 곡 상세정보 확인 가능

<img src='img/1.gif' align="right" width=1000>
<img src='img/2.gif' align="right" width=1000>  





















### 기능2. 비슷한 분위기의 곡 추천 가능 : 추천 년도 선택 -> 비슷한 분위기의 노래 리스트 생성  

<img src='img/3.gif' align="right" width=1000>  





















# K-Pop NLP Project

## 프로젝트 일정

: 간트차트

![image-20200930195006846](https://github.com/jiminAn/Kpop_NLP_Project/blob/master/img/1.png)

## 프로젝트 제안 발표

### 프로젝트 중간 제안 발표

[![팀뉴트로 : 프로젝트 제안 발표](https://img.youtube.com/vi/28hdOUgEhpc/0.jpg)](https://www.youtube.com/watch?v=28hdOUgEhpc&t=733s)

### 프로젝트 최종 제안 발표

[![팀뉴트로 : 프로젝트 제안 발표](https://img.youtube.com/vi/f8qpfL4log8/0.jpg)](https://www.youtube.com/watch?v=f8qpfL4log8)

## 핵심 코드

### 1. [Final_Data_Crawling](https://github.com/jiminAn/Kpop_NLP_Project/tree/master/Final_Data_Crawling) 파일

- `1992_1999_idol_get_id.ipynb` : 92~99년도 아이돌 고유 아이디 크롤링 코드
- `idol_list_with_id.csv ` : 92~99년도 멜론 아이디를 담은 csv 파일
- `melon_song_data_crawling.ipynb` : 멜론에서 곡 정보 크롤링 코드
- ` k_pop_92_99.tsv` : 최종 92~99년도 곡 정보 tsv 파일

### 2. [Final_LDA_Modeling]() 파일 

- ` preprocessing.ipynb` :  공통 전처리 코드(불용어 등)
-  LDA_`preprocess.ipynb` : LDA 모델에 맞는 형태로 데이터 전처리 코드
- `kpop_LDA_nva.ipynb`  : 가사에서 명사/동사/형용사를 추출하여 LDA 모델링 및 시각화 코드

### 3. [Final_LDA_Model_Training]() 파일 

  * `Model_training_try13.ipynb` : hyper-parameter 13개로 조정 후 테마 지정
  * `num=13.tsv` : 위 파일 실행 후 tsv형태로 저장한 파일 (곡별로 테마 열 추가된 형태)
  * `model_13.h5` : 학습시킨 모델을 저장한 파일

### 4. [Final_Pyqt5_UI]() 파일

- `prototype.py` : UI 디자인을 위한 prototype 선제작

  ![image-20200930195006846](https://github.com/jiminAn/Kpop_NLP_Project/blob/master/img/2.png)

- `app_ui` : pyqt5을 사용한 UI 코드

  


## 폴더

- folder [김준영](https://github.com/jiminAn/Kpop_NLP_Project/blob/master/%EA%B9%80%EC%A4%80%EC%98%81/README.md), [안지민](https://github.com/jiminAn/Kpop_NLP_Project/blob/master/%EC%95%88%EC%A7%80%EB%AF%BC/README.md), [이선우], [이은후](https://github.com/jiminAn/Kpop_NLP_Project/blob/master/%EC%9D%B4%EC%9D%80%ED%9B%84/README.md)

  : 팀원들의 개인 코드 수정 및 초안 버전 코드 저장 공간, 자세한 내용은 각 폴더의 README 파일(LOG.md)을 참고할 것

## [회의록](https://github.com/jiminAn/Kpop_NLP_Project/tree/master/%ED%9A%8C%EC%9D%98%EB%A1%9D)

: 온/오프라인으로 진행한 회의록을 yyyy_mm_dd.docx 파일로 정리하여 기록
