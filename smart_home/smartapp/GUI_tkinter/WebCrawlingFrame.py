import tkinter as tk
#import Naver_Ranking                    # 학원
#import OpenAPI_Dust                     # 학원
from smart_home.smartapp.GUI_tkinter.web_crawler.Naver_Ranking import main
from smart_home.smartapp.GUI_tkinter.web_crawler.OpenAPI_Dust import get_MicroDust


class WebCrawlFrame(tk.Frame):
    ip_entry = None
    port_entry = None
    message = None
    socket = None

    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):
        portal_frame = tk.LabelFrame(self, text='웹 크롤링')
        portal_frame.pack()
        portal_button = tk.Button(portal_frame, text='네이버 실시간 검색 순위')
        portal_button.pack(side='left')
        portal_button.bind('<Button-1>', self.on_naver_word_rank_click)

        portal_frame2 = tk.LabelFrame(self, text='Open API')
        portal_frame2.pack()
        portal_button2 = tk.Button(portal_frame2, text='미세먼지 확인하기')
        portal_button2.pack(side='left')
        portal_button2.bind('<Button-1>', self.on_air_status_click)


    def on_naver_word_rank_click(self,event): # event는 사용하지 않아도 이렇게 선언해야됨
        #Naver_Ranking.main()
        main()

    def on_air_status_click(self,event):
        #OpenAPI_Dust.get_MicroDust()
        get_MicroDust()
