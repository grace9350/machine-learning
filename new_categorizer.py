#문자간 유사도에는 Cosine distance 
#Bag of words 단어별로 인덱스 만들어 단어 개수 세기

#Process
#파일 불러오기
#파일 읽어서 단어사전(corpus) 만들기
#단어별로 index 만들기
#만들어진 인덱스로 문서별로 Bag of words vector 생성
#비교하고자 하는 문서 비교 (특정 문서와 다른 문서들간의 유사도 측정)
#얼마나 맞는지 측정 (0-1)

import os


def get_file_list(dir_name):
    return os.listdir(dir_name) #news_data 폴더에 있는 텍스트 파일 이름들 리스트에 넣기

def get_conetents(file_list):
    y_class = []
    X_text = []
    class_dict = { #야구는 0, 축구는 1
        1: "0", 2: "0", 3:"0", 4:"0", 5:"1", 6:"1", 7:"1", 8:"1"}

    for file_name in file_list:
        try:
            f = open(file_name, "r",  encoding="UTF8") #windows는 cp949로 읽어오기
            category = int(file_name.split(os.sep)[1].split("_")[0]) 
            #split(os.sep)[1] : sep은 백슬래시(\)로 구분하여 두번째로 오는 것 = 텍스트 파일 이름
            #split("_")[0] : '_'로 구분하여 맨 앞에 오는 것 = 숫자 
            #즉, 텍스트 이름의 맨 앞에 있는 숫자를 int로 바꿔서 category에 저장
            y_class.append(class_dict[category]) #야구에 관한건지 축구에 관한건지 구분하여 y_class에 추가 -> 4개 0, 1개 1
            X_text.append(f.read()) #파일 내용을 리스트에 저장 -> 총 15개의 문서 저장
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class


def get_cleaned_text(text): #단어의 의미없는 문장부호 제거
    import re
    text = re.sub('\W+','', text.lower() ) #소문자로 바꾼 뒤 문장부호 제거 (regular expression)
    return text


def get_corpus_dict(text):
    text = [sentence.split() for sentence in text] #2차원 리스트 - split() 리스트 생성 
    clenad_words = [get_cleaned_text(word) for words in text for word in words] #1차원 리스트

    from collections import OrderedDict
    corpus_dict = OrderedDict() #순서가 있는 사전
    for i, v in enumerate(set(clenad_words)): #set으로 중복 제거, enumerate로 인덱스와 값 추출
        corpus_dict[v] = i #v(단어)의 i(인덱스 번호)
    return corpus_dict


def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text] #two-dimension 원소는 각 단어의 인덱스 번호
    X_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))] #문서 수 X 단어 수 벡터의 원소 모두 0

    for i, text in enumerate(word_number_list): #i는 0 ~ 텍스트 수-1
        for word_number in text:
            X_vector[i][word_number] += 1 #각 텍스트마다 단어 수 갱신
    return X_vector

import math
def get_cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy) #두 텍스트의 cosine 값 구하기

def get_similarity_score(X_vector, source): #source는 찾고자 하는 문서
    source_vector = X_vector[source]
    similarity_list = []
    for target_vector in X_vector:
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector))
    return similarity_list #문서의 수 만큼의 list (source 텍스트도 포함)


def get_top_n_similarity_news(similarity_score, n):
    import operator
    x = {i:v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))

    return list(reversed(sorted_x))[1:n+1]

def get_accuracy(similarity_list, y_class, source_news):
    source_class = y_class[source_news]

    return sum([source_class == y_class[i[0]] for i in similarity_list]) / len(similarity_list)


if __name__ == "__main__":
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list] #os.path.join() 각 os에 맞게 적용되도록, +로 이어주면 X
    print(file_list) #"폴더이름 + 파일이름" 으로 경로 만들기
    print(len(file_list)) #3*5 = 15

    X_text, y_class = get_conetents(file_list)

    corpus = get_corpus_dict(X_text) #dict key: 단어, value: 인덱스
    print("Number of words : {0}".format(len(corpus)))
    X_vector = get_count_vector(X_text, corpus)
    source_number = 10 #10번째 텍스트와의 유사도 측정

    result = []

    for i in range(15):
        source_number = i

        similarity_score = get_similarity_score(X_vector, source_number)
        similarity_news = get_top_n_similarity_news(similarity_score, 10)
        print(similarity_news)
        accuracy_score = get_accuracy(similarity_news, y_class, source_number)
        result.append(accuracy_score)
    print(sum(result) / 15)