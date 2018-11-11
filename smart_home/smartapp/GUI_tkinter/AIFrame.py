import tkinter as tk
#import ai_light
from .ai_light import main
import keras
import numpy as np
import random
path = './sample/'
sample_name = 'DataSet.csv'


class AIFrame(tk.Frame):
    def __init__(self, master=None, cnf=None, **kw):
        super().__init__(master, cnf, **kw)
        self.create()

    def create(self):
        ai_frame = tk.LabelFrame(self, text='인공지능')
        ai_frame.pack()
        training_button = tk.Button(ai_frame, text='학습하기')
        training_button.pack(side='left')
        training_button.bind('<Button-1>', self.on_learning_click)

        test_button = tk.Button(ai_frame, text='테스트')
        test_button.pack(side='left')
        test_button.bind('<Button-1>', self.on_test_click)

    def on_learning_click(self, event):
        #ai_light.main()
        main()

    def on_test_click(self, event):
        model = keras.models.load_model('model.h5')
        # ## 예측하고 싶은 X값
        data_sample = [[3, 700, 0],
                       [18, 2250, 1],
                       [21, 1600, 0],
                       [12, 2700, 1],
                       [6, 745, 0],
                       [15, 2500, 0]]
        r = random.randrange(len(data_sample))
        print(r)
        X = np.array([3, 700, 0])

        # ## 실제 예측하기
        Y_results = model.predict(np.array([X]))
        Y_results = Y_results.argmax(axis=-1)
        Y_results = Y_results[0]
        print("%d시, 조도값(높을수록 밝음) %d, %d(1=주말,0=평일)"%(data_sample[r][0], data_sample[r][1], data_sample[r][2]))
        # ## 실제로 예측한 값(y)
        if Y_results == 0:
            print("불을 끈다")
        else:
            print("불을 켠다")


'''
1열 시간
2열 조도
3열 평일/주말 여부(주말 1)
4열 점등 여부
'''

'''
멀티노미어 classification 에서 쓰이는
one hot 인코딩

num_classes = int(max(ys) +1)  # [1],[1],[1],[4],[1], ...dlfjs tlrdml rkqt
Ys = keras.utils.to_categorical(ys, num_classes)
print(Ys) # 선형대수 값이 됐다 [0,0,0,1,0],[0,0,0,0,1], ...
대문자는 선형대수 값

x1->                                                        |   이 단계를 분류(classification)
        h(x)  --? y (여기까지 선형회귀 Linear Regresstion)  |   -> activation(계단함수) = 0 / 1
x2->                                                        |

(h(x)가 여러개라도 단일레이어임 ㅎ)

똑같은 파라미터를 가지고 여러개의 h(x)를 만들어서 조류인지 아닌지 파충류인지 아닌지를 구분

각각 h(x)의 결과가 0 , 1 ,0, ... 이런 식으로 도출(onehot 디코딩을 사용해서 1,1,4 값들을 [0,0,1] 식의 값으로 출력)


h(x)들을 단일 레이어라 부르고 또 다른 h(x)들을 거치면 딥러닝이 된다(단일레이어가 아니어야 딥러닝)
출력으로 나온 y값들이 다시 파라미터가 되어 다음 h(x)에 들어간다 

'''