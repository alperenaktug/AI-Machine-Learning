import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import os



# 1. Veriyi Oku
df = pd.read_excel("teknolojik_urunler_zamanli.xlsx")

# 2. Tarih sütununu düzelt
df['Tarih'] = pd.to_datetime(df['Tarih'])

# 3. Tarih'i indeks yap
df.set_index('Tarih', inplace=True)

def ekran_temizleme():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




def menu():
    print("Grafik Seçenekleri:") 
    print("1. Satışların Zaman içindeki değişimi (Çizgi Grafik)") 
    print("2. Aylık Toplam Satışlar (Bar Grafik)") 
    print("3. Kategorilere Göre Satış Dağılımı (Pasta Grafiği)")    
    print("4. Fiyat ve Satış İlişkisi (Scatter Plot)") 
    print("5. Fiyat Dağılım (Histogram)") 
    print("6. Aylık satış Miktarları (Çizgi Grafik)") 
    print("7. Fiyat Kategorisine Göre Toplam Satışlar (Bar Grafik)") 
    print("0. Çıkış Yap") 
    

    return int(input("Seçiminizi yapın:"))

# Kullanıcının seçimine göre ilgili işlemleri yapan fonksiyon

def grafik_secim(secilen):
    if secilen == 1:
        df['Satış'].plot(title='Satışların zaman içindeki değişimi' , xlabel='Tarih' , ylabel='Satış Miktarı')
        plt.show()
    elif secilen == 2:
        aylik_satis = df.resample('ME')['Satış'].sum()
        aylik_satis.plot(kind='bar', title='Aylık Toplam Satışlar')
        plt.xlabel('Ay')
        plt.ylabel('Toplam Satış Miktarı')
        plt.show()
    elif secilen == 3:
        kategori_satis = df.groupby('Kategori')['Satış'].sum()
        kategori_satis.plot(kind='pie', autopct='%1.1f%%', title='Kategorilere Göre Satış Dağılımı')
        plt.ylabel('')
        plt.show
    elif secilen == 4:
        z = np.polyfit(df['Fiyat (TL)'], df['Satış'], 1)
        p = np.poly1d(z)
        plt.plot(df['Fiyat (TL)'], p(df['Fiyat (TL)']), color='red')
        plt.show()
    elif secilen == 5:
        df['Fiyat (TL)'].plot(kind='hist', bins=10, title='Fiyat Dağılımı')
        plt.xlabel('Fiyat (TL)')
        plt.ylabel('Kategori')
        plt.show()  
    elif secilen == 6:
        aylik_satis = df.resample('ME')['Satış'].sum()
        aylik_satis.plot(kind='line', title='Aylık Satış Miktarları')
        plt.xlabel('Ay')
        plt.ylabel('Satış Miktarı')
        plt.show() 
    elif secilen == 7:
        bins = [0,2000,5000,10000,20000,30000]
        labels = ['Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Lüks']
        df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins=bins, labels=labels)
        df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar', title='Fiyat Kategorisine Göre Toplam Satışlar')
        plt.xlabel('Fiyat Kategorisi')
        plt.ylabel('Toplam Satış Miktarı')
        plt.show()

while True:
    ekran_temizleme()
    secim = menu()
    if secim == 0:
        print("Programdan çıkılıyor...")
        break
    elif 1 <= secim <= 7:
        grafik_secim(secim)
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
   

           
   























# 4. Grafik Çizimi

#df.plot(title='Satışların Zaman İçindeki Değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
#plt.grid(True)
# #plt.show()



# AYLIK SATIŞ TRENDİ

# aylik_satis = df.resample('ME').sum()
# aylik_satis.plot(kind='line', title='Aylık Satış Miktarları')
# plt.xlabel('Ay')
# plt.ylabel('Satış Miktarı')
# plt.show() 


# df.plot(kind='scatter', x='Fiyat (TL)' , y='Satış' , title='Fiyat ve Satış İlişkisi')

# z = np.polyfit(df['Fiyat (TL)'], df['Satış'], 1)
# p = np.poly1d(z)

# plt.plot(df['Fiyat (TL)'], p(df['Fiyat (TL)']), color='red')
# plt.show() 


# ÇOK İŞE YARAR

# bins = [0,2000,5000,10000,20000,30000]
# labels = ['Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Lüks']
# df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins=bins, labels=labels) """

# Fiyat Dağılımına Göre Satış Dağılımı

# df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar', title='Fiyat Kategorisine Göre Toplam Satışlar')
# plt.xlabel('Fiyat Kategorisi')
# plt.ylabel('Toplam Satış Miktarı')
# # plt.show()