# from gensim.models import Word2Vec
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
import scipy.spatial.distance

model = KeyedVectors.load('model.kv')


#ベクトルの計算
def calculate_language_vector(words):
    features = 300
    feature_vec = np.zeros((features),dtype = "float32")
    for word in words:
        try:
            feature_vec = np.add(feature_vec, model[word])
        except KeyError:
            pass
    if len(words) > 0:
        feature_vec = np.divide(feature_vec, len(words))
    return feature_vec

#最も類似したものを探す
def search_most_similar(emotion_vector):
    df = pd.read_csv('word_model.csv')
    max_lang = df.iloc[0,0]
    tmp_max =-1
    for i in range(len(df)):
        vect = calculate_language_vector(df.iloc[i,1])
        score = 1-scipy.spatial.distance.cosine(emotion_vector, vect)
        if score > tmp_max:
            max_lang = df.iloc[i,0]
            tmp_max = score
    return max_lang


#入力された選択肢のベクトルを計算する
def calculate_emotion_vector(key_list):
    feature_vec = np.zeros((300),dtype = "float32")
    for word in key_list:
        feature_vec = np.add(feature_vec, model[word])
    return feature_vec

