
import numpy as np

# Kitap Fiyatları
kitap_fiyatlari = np.array([75, 30, 15, 20, 10, 70, 50])

# Satılan Kitap Adetleri
satilan_kitap_adetleri = np.array([200, 300, 100, 440, 50, 110, 220])

# Kategoriler 
kategoriler = np.array(['Roman', 'Bilim', 'Çocuk', 'Tarih', 'Sanat', 'Teknoloji', 'Spor'])

# toplam_gelir = kitap_fiyatları * satılan_kitap_adetleri
# print("Toplam Gelir:", toplam_gelir)


ortalama_fiyat = np.mean(kitap_fiyatlari)
print("Ortalama Kitap Fiyatı:", ortalama_fiyat , 'TL')

max_fiyat = np.max(kitap_fiyatlari)
print("En Yüksek Kitap Fiyatı:", max_fiyat , 'TL')

min_fiyat = np.min(kitap_fiyatlari)
print("En Düşük Kitap Fiyatı:", min_fiyat , 'TL')


roman_fiyatları = kitap_fiyatlari[kategoriler == 'Roman']
print("Roman Kitap Fiyatları:", roman_fiyatları)  
# Roman kategorisindeki kitapların fiyatlarını filtreleyerek elde ediyoruz. kategoriler dizisinde 'Roman' olan indeksleri bulup, bu indekslere karşılık gelen kitap_fiyatları değerlerini alıyoruz.


# toplam_satis = np.sum(satılan_kitap_adetleri * kitap_fiyatları)
# print("Toplam Gelir :", toplam_satis)



veri = np.array([kitap_fiyatlari, satilan_kitap_adetleri])
veri_shaped = np.reshape(veri, (2, 7))
print(veri_shaped)





