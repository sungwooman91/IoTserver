import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime
import json
import csv
th_g_name = 'graph'
md_g_name = 'graph2'
save_path = 'D:\\installed\\xampp2\\htdocs\\graph\\'    # 집
#save_path = 'E:\\xampp\\htdocs\\graph\\'               # 학원
conv_file = 'conv.csv'


class GraphFrame(tk.Frame):
    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):
        th_frame = tk.LabelFrame(self, text='온도 습도')
        th_frame.pack()
        th_button = tk.Button(th_frame, text='온습도 그래프 확인')
        th_button.pack(side='left')
        th_button.bind('<Button-1>', self.on_th_graph_click)

        dust_frame = tk.LabelFrame(self, text='미세먼지')
        dust_frame.pack()
        dust_button = tk.Button(dust_frame, text='미세먼지 그래프 확인')
        dust_button.pack(side='left')
        dust_button.bind('<Button-1>', self.on_dust_graph_click)

    def on_th_graph_click(self, event):
        if not os.path.isdir('./sample/'):
            os.mkdir('./sample/')
        df = pd.read_csv('./sample/weather.csv', index_col=0, encoding='utf-8')

        # time_df = df.iloc[:,0:0] # '1행 1열'~'8행 1열'까지 가져옴
        time_df = df.iloc[:, 0:2]
        ax = time_df.plot(kind='bar', title='weather', figsize=(6, 4), legend=True, fontsize=12)
        ax.set_xlabel('hour', fontsize=12) # x 축 정보 표시
        ax.set_ylabel('Temperatures/Humidity', fontsize=12)
        ax.legend(['Temperatures','Humidity'], fontsize=12)     # 범례 지정

        if not (os.path.isdir(save_path)):  # 해당 경로에 폴더 있는지 확인
            os.mkdir(save_path)  # 없으면 새로 생성

        now = datetime.datetime.now()
        now = now.strftime('%Y%m%d')

        plt.savefig(save_path+th_g_name+now+".png", dpi=100)
        plt.show()

    def on_dust_graph_click(self, event):
        big_list = []
        data_list = []

        for i in range(1,6):
            with open('./sample/통합대기환경정보_신암동'+str(i) + '.json') as f:
                data = json.load(f)
                data_list.append(data[0]["dataTime"])
                data_list.append(data[0]["pm10Value"])
                data_list.append(data[0]["pm25Value"])
                big_list.append(data_list)
                data_list=[]

        f = open('./sample/'+conv_file, 'w', encoding='utf-8', newline='') ##################### json 파일을 열어서 conv.csv 파일로 저장후 그래프로 만듬
        wr = csv.writer(f)
        for i in range(0,5):
            wr.writerow(big_list[i])
        f.close()

        df = pd.read_csv('./sample/conv.csv', index_col=0, encoding='utf-8')
        time_df = df.iloc[:, 0:2]
        ax = time_df.plot(kind='bar', title='micro_dust', figsize=(6, 4), legend=True, fontsize=12)
        ax.set_xlabel('hour', fontsize=12)  # x 축 정보 표시
        ax.set_ylabel('pm10Value/pm2.5Value', fontsize=12)
        ax.legend(['pm10Value', 'pm2.5Value'], fontsize=12)

        if not (os.path.isdir(save_path)):  # 해당 경로에 폴더 있는지 확인
            os.mkdir(save_path)  # 없으면 새로 생성

        now = datetime.datetime.now()
        now = now.strftime('%Y%m%d')

        plt.savefig(save_path+md_g_name+now+".png", dpi=100)
        plt.show()


# index_col - https://datascienceschool.net/view-notebook/c5ccddd6716042ee8be3e5436081778b/
# ix, iloc, loc 예제를 통한 구분 - https://dandyrilla.github.io/2017-08-12/pandas-10min/
# iloc 사용 - https://code-examples.net/ko/q/ac346d
# 전체 틀 참조 - https://dojang.io/mod/page/view.php?id=1159