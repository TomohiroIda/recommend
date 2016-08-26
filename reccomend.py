import numpy
import numpy as np
import pandas as pd

def data():
    pd.read_csv('data.csv')

#相関係数を求める関数の定義
def f(x,y):
    numpy.corrcoef(x, y)[0][1]

def pearson(item, rating):
    for i in range(1,943):
        data1  =data.loc[data.user==i,['item','rating']]#ユーザーiのデータのみを抽出
        a_item = set(item)
        s_item = set(list(data.loc[data.user == i,'item'])

    if len(a_item & s_item) <= 1:
            print("corr" = 0)#活動ユーザーと標本ユーザーの間に共通の評価アイテムが存在しない場合は相関係数が0
    else:
        print("corr" = f(np.array(data1.loc[data1['item'].isin(a_item & s_item),'rating']),np.array(rating)))#活動ユーザーと標本ユーザーの相関係数を計算

    print("You are similer to the user",max(f(np.array(data1.loc[data1['item'].isin(a_item & s_item),'rating']),np.array(rating)), key=(lambda i:f(np.array(data1.loc[data1['item'].isin(a_item & s_item),'rating']),np.array(rating))[i])))
    #相関係数が最大となる標本ユーザーを表示する








