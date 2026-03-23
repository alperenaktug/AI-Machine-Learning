
import pandas as pd

df = pd.read_excel('teknolojik_urunler1.xlsx')


# eksik_veri = df.isnull()
# print(eksik_veri)
# Tabloada eksik verileri true olarak gösterir.


# temiz_veri = df.dropna()
# print(temiz_veri)
# eksik değerleri df den siler.


# doldurulmus_df = df.fillna("Değer yok")
# print(doldurulmus_df)
# dataframe de boş olan yerlere değer atama 


# df['Fiyat (TL)'] = df['Fiyat (TL)'].astype("float")
# print(df.dtypes)
# Daataframe de ki fiyat sütunun veri tipini değiştirir.


# df.insert(2,'New Sütun' , range(1,21))
# print(df.head())
# Dataframe e yeni bir sütun ve sütunda hangi verilerin olacağı eklendi.


# df.to_excel('to_new.xlsx' , index =False)
# print("Veri kaydedildi!")


# df_düsük = df.sort_values(by='Fiyat (TL)' , ascending=False)
# print(df_düsük)
# Dataframe de Fiyat sütununu büyükten küçüğe sıralandı.





