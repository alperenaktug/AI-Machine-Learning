
import pandas as pd

df = pd.read_excel('teknolojik_urunler.xlsx')


# df_fiyat_ust = df[df['Fiyat (TL)'] > 5000]
# print(df_fiyat_ust)
# Dataframe de fiyatı 5000 tl den yüksek olanları getir.


# df_filtreli = df[(df['Fiyat (TL)'] > 5000) & (df['Kategori'] == 'Bilgisayarlar')]
# print(df_filtreli)
# Fiyatı 5000 ve üzeri olanlar ile kategorisi bilgisayarlar olanı getir.


# df_secili = df.loc[:, ['Ürün Adı' , 'Fiyat (TL)']]
# print(df_secili)
# df.loc sütun seçicem diyorum  bu iki sütun bilgilerini getir diyorum : ile bundan öncekileri
# getirme diyorum.


# df_ilk = df.iloc[:5,:]
# print(df_ilk)
#bu kod 0, 1, 2, 3 ve 4. satırları (toplam 5 satır) getirir.


# df_kategoriler = df[df['Kategori'].isin(['Televizyonlar','Mobil Cihazlar'])]
# print(df_kategoriler)
# Dataframe de isin() fonksiyonu ile Kategoriler kısmında televizyon ve mobil cihaz verileri var
# mı bu verileri getiriyoruz string değerler üzerinde kullanılır.