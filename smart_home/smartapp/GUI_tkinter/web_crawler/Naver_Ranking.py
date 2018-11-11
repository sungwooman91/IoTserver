import os
import time
import datetime
import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

folder_path = 'D:\\1\\NEW\\smart_home/'             # 집 경로
folder_name = 'rank_word/'                          # 저장할 폴더명


def main():
    html = urllib.request.urlopen('https://www.naver.com/')
    soup = BeautifulSoup(html, 'html.parser')

    search_word = soup.findAll('span', attrs={'class': 'ah_k'})
    rank_data = soup.findAll('span', attrs={'class': 'ah_r'})

    word_list = []
    rank_list = []  # 검색어 목록이 정렬되어 있어서 사실 안 구해도 됨...
    rank = 20

    result = []
    for i in range(rank):
        word_list.append(search_word[i].text)
        rank_list.append(rank_data[i].text)
        result.append([rank_list[i]] + [word_list[i]])

    for i in result:
        print(i)

    word_table = DataFrame(result, columns=('순위', '검색어'))
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d')
    now = now + '_' + time.strftime('%H%M%S')           # 현재 시간을 반환하는 함수

    file_name = "realtime_search_word_rank_" + now + ".csv"



    if not (os.path.isdir(folder_path + folder_name)):  # 해당 경로에 폴더 있는지 확인
        os.mkdir(folder_path + folder_name)             # 없으면 새로 생성

    file_path = folder_path + folder_name
    word_table.to_csv(file_path + file_name, encoding="cp949", mode='w', index=False) # 집에서 한글 깨짐 방지
    #word_table.to_csv(file_path + file_name, encoding="utf-8", mode='w', index=False) # 학원에선 이게 깨짐

    print(file_path + file_name+" Saved")
    return result

if __name__ == "__main__" :
    main()