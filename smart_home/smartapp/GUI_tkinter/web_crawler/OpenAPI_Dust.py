import urllib.request
import datetime, time
import json
import os

access_key = "iIhsixEf18XxhFwut8lRVPkptX44Z0E2kGCTBl8%2BBnOUU%2BNX5QoSpXcwZ1J14NbOB1s2cxLv9Uuf%2F%2FkjnHzysQ%3D%3D"
ver_info = "1.3"
pageno = "1"
numofrows = "20"

now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d')
now = now + '_' + time.strftime('%H%M%S')                       # 현재 시간 반환

folder_path = 'D:\\1\\NEW\\smart_home\\micro_dust\\'                        # 절대경로(집)
#folder_path = 'D:\\2\smart_home/micro_dust\\'                   # 절대경로(학원)

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as Error_msg:
        print(Error_msg)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getMicroDustURL(sidoName):
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_returnType=json&serviceKey=" + access_key       # 리턴타입 오타나면 기본형인 xml로 받아버림
    parameters += "&sidoName=" + urllib.request.quote(sidoName)     # sidoName=한글변수. ascii->utf-8로 됨. 무시하면 오류남
    parameters += "&pageNo=" + pageno
    parameters += "&numOfRows=" + numofrows
    parameters += "&ver=" + ver_info

    url = end_point + parameters

    result_data = get_request_url(url)
    if result_data is None: # 데이터가 하나도 없다면~
        return None
    else:
        return json.loads(result_data)


def get_MicroDust(sidoName='대구',townName='신암동'):
    jsonData = getMicroDustURL(sidoName)
    jsonResult = []

    if jsonData is None: # 크롤링 실패시 아무것도 없음
        return -1

    for i in jsonData['list']:
        if townName == i['stationName']:
            print(i['stationName'])
            jsonResult.append({'pm10Value': i['pm10Value'],
                               'pm25Value':i['pm25Value'],
                               'dataTime':i['dataTime']})
            break   # 원하는 데이터를 받는 즉시 탐색 종료

    if not (os.path.isdir(folder_path)):   # 해당 경로에 폴더 있는지 확인
        os.mkdir(folder_path)               # 없으면 새로 생성
    with open(folder_path+'통합대기환경정보_%s%s%s.json' %(sidoName,townName,now), 'w', encoding='utf8') as outfile:
        resultJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(resultJson)

    print(folder_path+'통합대기환경정보_%s%s%s.Json SAVED' %(sidoName,townName,now))
    return jsonResult