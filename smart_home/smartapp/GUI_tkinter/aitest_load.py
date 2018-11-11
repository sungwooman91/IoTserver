# coding: utf-8
import keras
import numpy as np

# ## 모델 불러오기
model = keras.models.load_model('model.h5')
# ## 예측하고 싶은 X값
X = np.array([3, 2400, 1])

# ## 실제 예측하기
Y_results = model.predict(np.array([X]))
y_results = Y_results.argmax(axis=-1)
y_result = y_results[0]

# ## 실제로 예측한 값(y)
print(y_result)