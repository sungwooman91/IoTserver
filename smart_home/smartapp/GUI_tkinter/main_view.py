import tkinter as tk
from tkinter import ttk

#   import ServerFrame
#   from .Server Frame import Server (== from __main__.Server_Frame import Server)
#   from smart_home.smartapp.GUI_tkinter.ServerFrame import Server # cmd 창에서 실행이 안됐음
#   from smartapp.GUI_tkinter.ServerFrame import Server     # WebCrawlingFrame에서 모듈 임포트 오류발생 (import OpenAPI_Dust)
from smart_home.smartapp.GUI_tkinter.ServerFrame import Server
from smart_home.smartapp.GUI_tkinter.WebCrawlingFrame import WebCrawlFrame
from smart_home.smartapp.GUI_tkinter.GraphFrame import GraphFrame
from smart_home.smartapp.GUI_tkinter.AIFrame import AIFrame

window = tk.Tk()
window.title('Main Window')
window.geometry('360x240+500+200')  # 가로X세로 크기 + x위치, y위치

main_frame = tk.Frame(window)
main_frame.pack(expand=True, fill='both')

tabs = ttk.Notebook(main_frame)
tabs.pack(expand=True, fill='both')

#server_frame = ServerFrame.Server(tabs) #import ServerFrame 사용시
server_frame = Server(tabs) # from .ServerFrame import Server 사용시
tabs.add(server_frame, text='수동 제어')

webcrawling_frame = WebCrawlFrame(tabs)
tabs.add(webcrawling_frame, text='웹 크롤러')

graph_frame = GraphFrame(tabs)
tabs.add(graph_frame, text='그래프')

ai_frame = AIFrame(tabs)
tabs.add(ai_frame, text='인공지능')

main_frame.mainloop()