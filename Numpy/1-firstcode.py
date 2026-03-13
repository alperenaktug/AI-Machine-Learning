import numpy as np


dizi1 = np.array([1, 2, 3, 4, 5])  
print(dizi1)
# Bir diziyi yazdırmak için numpy kütüphanesini kullanarak bir dizi oluşturduk ve ardından bu diziyi ekrana yazdırdık.


dizi2 = np.arange(0,20,2)
print(dizi2)
# np fonksiyonunu kullanarak 0'dan başlayarak 20'ye kadar olan çift sayıları içeren bir dizi oluşturduk ve bu diziyi ekrana yazdırdık.


dizi3 = np.linspace(0, 10, 20)
print(dizi3)
# np.linspace fonksiyonunu kullanarak 0 ile 10 arasında eşit aralıklı 20 sayı içeren bir dizi oluşturduk ve bu diziyi ekrana yazdırdık.


boyut = dizi1.ndim
data_type = dizi1.dtype

print("Dizinin boyutu:", boyut)
print("Dizinin veri tipi:", data_type)
# dizi1'in boyutunu ve veri tipini öğrenmek için ndim ve dtype özelliklerini kullandık ve sonuçları ekrana yazdırdık.
