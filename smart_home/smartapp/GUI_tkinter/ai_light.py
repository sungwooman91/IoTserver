# coding: utf-8
import pandas as pd
import numpy as np
import keras


def main():
    df = pd.read_csv('./sample/DataSet.csv')
    # numpy array로 변환
    dataset = df.values
    Xs = dataset[0:, :-2]
    Xs = Xs.astype(int)
    
    Xs_test = dataset[0:, :-2]
    Xs_test = Xs_test.astype(int)
    
    ys = dataset[:, -2:-1]
    ys = ys.astype(int)
    ys_test = dataset[:, -2:-1]
    ys_test = ys_test.astype(int)
    
    model = keras.models.Sequential()
    
    layer = keras.layers.Dense(16, input_dim=3, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros')
    model.add(layer)
    
    layer = keras.layers.Dense(1, activation='sigmoid', kernel_initializer='random_uniform', bias_initializer='zeros')
    model.add(layer)
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    model.fit(Xs, ys, epochs=1000, batch_size=10)
    
    y_results = model.predict(Xs)
    
    print('실제값 : ', ys.flatten().astype(int))
    print('예측값 : ', np.rint(y_results.flatten()).astype(int))
    
    score = model.evaluate(Xs_test, ys_test)
    print('loss=', score[0])
    print('accuracy=', score[1])    # accuracy - 정확성
    
    model.save('model.h5')