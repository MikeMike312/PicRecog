#綾鷹を選ばせるプログラム

from keras import models
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np

#保存したモデルの読み込み
model = model_from_json(open('C:/Users/mizuki/ttf_test/inst_predict.json').read())
#保存した重みの読み込み
model.load_weights('C:/Users/mizuki/ttf_test/inst_predict.hdf5')

categories = ["bass","drums","mic","guiter"]

#画像を読み込む
img_path = str(input())
img = image.load_img(img_path,target_size=(150, 150, 3))
x = image.img_to_array(img)/255
x = np.expand_dims(x, axis=0)

#予測
features = model.predict(x)

#予測結果によって処理を分ける
if features[0,0] == np.max(features[0,:]):
    print ("選ばれたのは、bassでした。")
    print(features)
#elif features[0,4] == 1:
#    print ("選ばれたのは、綾鷹（茶葉のあまみ）でした。")

else:
    for i in range(0,3):
          if features[0,i] == np.max(features[0,:]):
              cat = categories[i]
    print(features[0,i])
    print(features)
    message = "違います（もしかして：あなたが選んでいるのは「" + cat + "」ではありませんか？）"
    print(message)