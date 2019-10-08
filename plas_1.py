from PIL import Image
import os, glob
import numpy as np
import random, math

# 画像が保存されているディレクトリのパス
root_dir = "C:/Users/mizuki/ttf_test"
# 画像が保存されているフォルダ名
categories = ["bass","drums","mic","guiter"]

X = [] # 画像データ
Y = [] # ラベルデータ

# フォルダごとに分けられたファイルを収集
#（categoriesのidxと、画像のファイルパスが紐づいたリストを生成）
allfiles = []
for idx, cat in enumerate(categories):
    image_dir = root_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    for f in files:
        allfiles.append((idx, f))

for cat, fname in allfiles:
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((150, 150))
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)

x = np.array(X)
y = np.array(Y)

np.save("# モデルの精度を測る

#評価用のデータの読み込み
eval_X = np.load("C:/Users/mizuki/ttf_test/tea_data_test_X_150.npy")
eval_Y = np.load("C:/Users/mizuki/ttf_test/tea_data_test_Y_150.npy")

#Yのデータをone-hotに変換
from keras.utils import np_utils

test_Y = np_utils.to_categorical(test_Y, 10)

score = model.model.evaluate(x=test_X,y=test_Y)

print('loss=', score[0])
print('accuracy=', score[1])/tea_data_test_X_150.npy", x)
np.save("C:/Users/mizuki/ttf_test/tea_data_test_Y_150.npy", y)

# モデルの精度を測る

#評価用のデータの読み込み
eval_X = np.load("C:/Users/mizuki/ttf_test/tea_data_test_X_150.npy")
eval_Y = np.load("C:/Users/mizuki/ttf_test/tea_data_test_Y_150.npy")

#Yのデータをone-hotに変換
from keras.utils import np_utils

test_Y = np_utils.to_categorical(test_Y, 10)

score = model.model.evaluate(x=test_X,y=test_Y)

print('loss=', score[0])
print('accuracy=', score[1])