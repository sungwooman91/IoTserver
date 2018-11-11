import tkinter as tk
from socket import socket

SERVER_IP = '192.168.0.2'
SERVER_PORT = '7777'


class Server(tk.Frame):

    message = None
    socket = None

    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):

        # Server Address
        net_frame = tk.LabelFrame(self, text='Server Address')
        net_frame.pack(fill='x')
        ip_label = tk.Label(net_frame, text='IP : ')
        ip_label.pack(side='left')
        self.ip_entry = tk.Entry(net_frame)
        self.ip_entry.pack(side='left', expand=True, fill='x')
        self.ip_entry.insert(tk.END, SERVER_IP)

        port_label = tk.Label(net_frame, text='PORT : ')
        port_label.pack(side='left')
        self.port_entry = tk.Entry(net_frame, text='77')
        self.port_entry.pack(side='left', expand=True, fill='x')
        self.port_entry.insert(tk.END,'7777')

        # LIGHT
        light_frame = tk.LabelFrame(self, text='조명')
        light_frame.pack()
        light_on_button = tk.Button(light_frame, text='조명 켜')
        light_on_button.pack(side='left')
        light_on_button.bind('<Button-1>', self.on_click)
        light_off_button = tk.Button(light_frame, text='조명 꺼')
        light_off_button.pack(side='left')
        light_off_button.bind('<Button-1>', self.on_click)

        # 창문
        window_frame = tk.LabelFrame(self, text='창문')
        window_frame.pack()
        window_open_button = tk.Button(window_frame, text='창문 열어')
        window_open_button.pack(side='left')
        window_open_button.bind('<Button-1>', self.on_click)
        window_close_button = tk.Button(window_frame, text='창문 닫아')
        window_close_button.pack(side='left')
        window_close_button.bind('<Button-1>', self.on_click)

        # 커튼
        curtain_frame = tk.LabelFrame(self, text='커튼')
        curtain_frame.pack()
        curtain_open_button = tk.Button(curtain_frame, text='커튼 걷어')
        curtain_open_button.pack(side='left')
        curtain_open_button.bind('<Button-1>', self.on_click)
        curtain_close_button = tk.Button(curtain_frame, text='커튼 쳐')
        curtain_close_button.pack(side='left')
        curtain_close_button.bind('<Button-1>', self.on_click)


        self.message = tk.Message(self, text='No Message...', relief='solid', width='400')
        self.message.pack(expand=True, fill='both')

    def on_click(self, event):
        widget = event.widget
        widget_text = widget.cget('text') # LabelFrame에 적힌 text를 그대로 가져온다
        print(widget_text)##############
        self.send_to_server(widget_text)

    def send_to_server(self, send_msg):
        ip = self.ip_entry.get()
        port = self.port_entry.get()

        with socket() as self.socket:
            self.socket.connect((ip, int(port)))
            self.socket.sendall(send_msg.encode())
            recv_msg = self.socket.recv(1024) ########## 서버로부터 받은 메세지
            # print(recv_msg) # decode 필요함!!!
            self.message.configure(text='Received Message : ' + recv_msg.decode())
            # print(f'>{resp.decode()}')