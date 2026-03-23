
import pandas as pd

df = pd.read_excel('teknolojik_urunler.xlsx')
#excel dosyasını okuma işlemi

#print(df.head())
# il bir kaç satırı getirdi

# average_price = df['Fiyat (TL)'].mean()
# print(f"Ortalama Fiyat : {average_price}")
# Dataframe deki ortalama fiyat bilgisini getirdik


# category_bazında_satıs = df.groupby('Kategori')['Satış'].sum()
# print(category_bazında_satıs)
# Kategori bazında ürünlerin satış toplamını veriyor.


# max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
# print(max_gelir)
# ençok gelir getiren ürün
# loc() -> belirli bir sütun üzerinde çalışacağımın bilgisini verir.
# idxmax -> istenilen değerin max değerini getirir.


# fiyati_ust_olanlar = df[df['Fiyat (TL)'] > 4000]
# print("Fiyatı 4000 TL üstü ürünler : " )
# print(fiyati_ust_olanlar)
# fiyati_ust_olanlar.to_excel('fiyati_4000_ust_olanlar.xlsx' , index=False)
# Fiyatı 4000 üstünde olanları getir ve excel ile dışarı yazdırma işlemi


# urun_adi = df['Ürün Adı']
# print(urun_adi)
# Ürün adını sütununu getirme işlemi yapar.


