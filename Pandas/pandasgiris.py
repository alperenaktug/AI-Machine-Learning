
import pandas as pd

# s = pd.Series([10,20,30,40,50] , index=["A","B","C","D","E"])
# # Series() dizi üzerinde satır ve sütunlarda işlem yaparken kullanırız.
# # indes() satır başlıklarına isim vermede kullanırız.

# print(s)



data = {
  'Kategori':["Roman","Tarih","Bilim","Çocuk"],
  'Fiyat':[23,54,65,76],
  'Satış Adedi':[2,5,7,8]
}

df = pd.DataFrame(data)
# print(df)

# print(df.head())
# print(df.head(2))
# Bir veri çerçevesinin ilk bir kaç satırını direk getirmede yardımcı olur.

# print(df.info())
# Dataframe mimarisi hakkında bilgi verir

# print(df.describe())
# Dataframe sayısal sütunları analiz eder ve hızlıca bir matematiksel özet sunar.


# print(df[['Kategori'],['Satış Adedi']])

# filtre = df[df['Fiyat'] > 50]
#Dataframe de Fiyatı 50 den büyük olanları listeleme
# print(filtre)


df['Toplam Gelir:'] = df['Fiyat'] * df['Satış Adedi']
# DataFrame e Toplam gelir sütununu ekledi 
print(df)

df = df.drop('Kategori' , axis=1)
# Kategori sütununu sileriz burada
print(df)

