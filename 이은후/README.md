# LOG
-----------------
## 1. [song crawling](https://github.com/jiminAn/Kpop_NLP_Project/tree/master/%EC%9D%B4%EC%9D%80%ED%9B%84/song%20crawling) 파일: 멜론 사이트에서 아이돌 노래정보 크롤링
  * `try2_create_idol_id(.ipynb)` 90년대 가수들 대상 멜론에서 부여된 id 크롤링
  * `idol_list_with_id(.csv)` 위 파일 실행 후 csv형태로 저장한 파일 (각 아이돌별 id열 추가된 형태)
  * `94to95_idol_list(.csv)` 위 파일 중 담당년도(94,95)에 해당하는 가수들만 따로 저장한 파일
  * `melon_crawling20(.ipynb)` 담당년도 가수당 곡 인기순 정렬 후 20개씩 곡정보 크롤링
  * `94_95_kpop_final(.tsv)` 위 파일 실행 후 tsv형태로 저장한 파일 (최종파일)
  

## 2. [modeling](https://github.com/jiminAn/Kpop_NLP_Project/tree/master/%EC%9D%B4%EC%9D%80%ED%9B%84/modeling) 파일: 노래가사 대상으로 LDA모델, K-means 적용
  * `preprocess(.ipynb)` 알고리즘 적용 위해 필요한 형태로 데이터 전처리  
  * **[LDA] 파일**
    * `LDA modeling_(.ipynb)` (추가 전처리 후) 노래가사(한글+영어) LDA모델 적용하여 테마별 시각화
  * **[K-means] 파일**
    * `k-means(.ipynb)` 노래가사(한글+영어) k-means알고리즘 적용하여 군집별로 클러스터링
    
    
## 3. [Model training](https://github.com/jiminAn/Kpop_NLP_Project/tree/master/%EC%9D%B4%EC%9D%80%ED%9B%84/Model%20training) 파일: 노래 테마분류 정확도 위해 모델 학습
  * `Model_training_try13(.ipynb)` hyper-parameter 13개로 조정 후 테마 지정
  * `num=13(.tsv)` 위 파일 실행 후 tsv형태로 저장한 파일 (곡별로 테마 열 추가된 형태)
  * **[trained data] 파일**
    * `model_13(.h5)` 위에서 학습시킨 모델 저장한 파일
