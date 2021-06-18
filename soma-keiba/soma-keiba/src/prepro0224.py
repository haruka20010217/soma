# dfを確認
import pandas as pd
df = pd.read_csv("./data/csv_files/df.csv")
df


# dfのカラムの型を確認
df.dtypes


# dfの欠損値の有無を確認(Trueなら、欠損値あり)
df.isnull().any(axis=0)



# 欠損値がある行を削除したものをdf2に
df2 = df.dropna(how='any', axis=0)


# df2の欠損値の有無を確認(Trueなら、欠損値あり)
df2.isnull().any(axis=0)



# df2["タイム"]をobjectからfloatに
for i in range(len(df2["タイム"])):
    if isinstance(df2["タイム"].iloc[i], float):
        pass
    else:
        lst = list(map(float, df2["タイム"].iloc[i].split(":")))
        df2["タイム"].iloc[i] = lst[0] * 60 + lst[1]

df2["タイム"] = df2["タイム"].astype(float)


#df2[馬体重]とdf2["増減"]を分ける
df2["体重"] = 0
df2["増減"] = 0

for i in range(len(df2["馬体重"])):
    lst = list(map(int, df2["馬体重"].iloc[i].strip(")").split("(")))
    df2["体重"].iloc[i] = lst[0]
    df2["増減"].iloc[i] = lst[1]

del df2["馬体重"]


# df2["性別"]、df2["年齢"]に分ける
df2["性別"] = 0
df2["年齢"] = 0

for i in range(len(df2["性齢"])):
    lst = list(df2["性齢"].iloc[i])
    df2["性別"] = lst[0]
    df2["年齢"] = lst[1]

df2["年齢"] = df2["年齢"].astype(int)

del df2["性齢"]


# df2["着順"]をintに
df2["着順"] = df2["着順"].astype(int)


# df2["単勝"]をfloatに
df2["単勝"] = df2["単勝"].astype(float)


# df2["賞金(万円)"]をdf2["賞金"]に
df2["賞金"] = df2["賞金(万円)"]
del df2["賞金(万円)"]


# df2["賞金"]をfloatに
for i in range(len(df2["賞金"])):
    df2["賞金"].iloc[i] = df2["賞金"].iloc[i].replace(",", "")

df2["賞金"] = df2["賞金"].astype(float)




# df2の確認
df2

