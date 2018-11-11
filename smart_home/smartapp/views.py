from django.http import HttpResponse
from .GUI_tkinter.web_crawler import OpenAPI_Dust
from .GUI_tkinter.web_crawler import Naver_Ranking
import json

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_data(request):
    id = request.GET['id']      # id라는 내용만 가져옴
    kind = request.GET['kind']

    print(kind)

    #if id != 'android':     # id가 android가 아닌 경우 이 리퀘스트를 실행하지 않음.
    #    return -1

    if kind == 'dust': # 미세먼지 라는 메세지 일때는 이런 요청
        sido = request.GET['sido']  # sido 라는 내용만 가져옴
        gudong = request.GET['gudong']
        print(sido, gudong)
        dusts = OpenAPI_Dust.get_MicroDust(sido, gudong)
        dusts = {'dusts': dusts}
        result_json = json.dumps(dusts, ensure_ascii=False)

    elif kind=='ranking' :
        ranks = Naver_Ranking.main()
        rank = {'ranks': ranks}
        result_json = json.dumps(rank, ensure_ascii=False)

    print(result_json)
    return HttpResponse(result_json)