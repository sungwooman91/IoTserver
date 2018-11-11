# coding: utf-8
import pandas as pd
import keras

df = pd.read_csv('./sample/DataSet.csv')
# ## numpy array로 변환
dataset = df.values
# ## dataset을 Xs와 Ys로 나누기

Xs = dataset[:, :-2]
Xs = Xs.astype(int)

Ys = dataset[:, -2:]
Ys = Ys.astype(int)

# ## ys를 Ys로 OneHot 인코딩하기

#num_classes = int(max(ys) + 1) # 1부터 시작하기 때문에 +1
#Ys = keras.utils.to_categorical(ys, num_classes) # onehot encoding

# ## 모델 생성 및 Activation 설정

model = keras.models.Sequential()

#layer = keras.layers.Dense(num_classes, input_dim=Xs.shape[1], activation='softmax')
layer = keras.layers.Dense(2, input_dim=Xs.shape[1], activation='softmax') # input_dim 입력층(시간/조도/평일,주말 여부) 첫번째 파라미터 = 출력층 갯수
model.add(layer)

# ## Optimaizer 설정 (Gradient Descent 또는 Adam)

# sgd = keras.optimizers.SGD(lr=0.01)
# model.compile(optimizer=sgd)
model.compile(loss='categorical_crossentropy', optimizer='adam')
#adam Algorithm ≒ Gradient Descent Algorithm

# ## 학습시키기
model.fit(Xs, Ys, epochs=200, batch_size=10)

# 샘플링 테스트
Y_results = model.predict(Xs)

# OneHot Encoding된 Y값을 argmax함수로 y값으로 만듬
Y_results = Y_results.argmax(axis=-1)

print('실제값 : ', Ys.flatten())
print('예측값 : ', Y_results)

# ## 학습된 모델 저장하기
model.save('model.h5')
# 학습이 정상적으로 진행되지 않아서 이 코드 사용을 중지하고 레이어를 
