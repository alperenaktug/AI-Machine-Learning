

import numpy as np

dizi1 = np.array([1, 2, 3, 4])
dizi2 = np.array([6, 7, 8, 9])


# toplam = dizi1 + dizi2
# çıkartma = dizi1 - dizi2
# carpma = dizi1 * dizi2
# bölme = dizi1 / dizi2

# print("Toplam :",toplam)
# print("Fark : ",çıkartma)
# print("Çarpma : ",carpma)
# print("Bölme : ",bölme)

# Bu işlemler, dizilerin her bir elemanına sırayla uygulanır. Örneğin, toplama işlemi için dizi1'in ilk elemanı olan 1, dizi2'nin ilk elemanı olan 6 ile toplanır ve sonuç 7 olur. Bu işlem tüm elemanlar için tekrarlanır ve sonuç olarak yeni bir dizi elde edilir.

toplam1 = np.sum(dizi1)
toplam2 = np.sum(dizi2)
print("Dizi1'in elemanlarının toplamı :",toplam1)
print("Dizi2'in elemanlarının toplamı :",toplam2)

# np.sum() fonksiyonu, bir dizinin tüm elemanlarının toplamını hesaplar. Bu fonksiyon, dizinin boyutuclear
# na bakılmaksızın çalışır ve tüm elemanları toplar.

carpim = np.prod(dizi1)
print("Dizi1'in elemanlarının çarpımı :",carpim)

# np.prod() fonksiyonu, bir dizinin tüm elemanlarının çarpımını hesaplar. Bu fonksiyon da dizinin boyutuna bakılmaksızın çalışır ve tüm elemanları çarparak sonucu verir.

kareal = np.square(dizi1)
print("Dizi1'in elemanlarının kareleri :",kareal)

# np.square() fonksiyonu, bir dizinin her bir elemanının karesini hesaplar. 

kokal = np.sqrt(dizi1)
print("Dizi1'in elemanlarının karekökleri :",kokal)

# np.sqrt() fonksiyonu, bir dizinin her bir elemanının karekökünü hesaplar. Bu fonksiyon, pozitif sayılar için geçerlidir ve negatif sayılar için NaN (Not a Number) sonucu verir.

# ARİTMETİK ORTALAMA :

ortalama1 = np.mean(dizi1)
ortalama2 = np.mean(dizi2)
print("Dizi1'in aritmetik ortalaması :",ortalama1)
print("Dizi2'in aritmetik ortalaması :",ortalama2)

# np.mean() fonksiyonu, bir dizinin aritmetik ortalamasını hesaplar. ılır.


# MEDYAN :

medyan1 = np.median(dizi1)
medyan2 = np.median(dizi2)  
print("Dizi1'in medyanı :",medyan1)
print("Dizi2'in medyanı :",medyan2)

# np.median() fonksiyonu, bir dizinin medyanını hesaplar. Medyan, bir veri setindeki ortanca değeri temsil eder. Eğer veri seti tek sayıda eleman içeriyorsa, medyan ortadaki eleman olur. Eğer veri seti çift sayıda eleman içeriyorsa, medyan ortadaki iki elemanın aritmetik ortalaması olarak hesaplanır.


# STANDART SAPMA :


standartsapma = np.std(dizi1)
print("Dizi1'in standart sapması :",standartsapma)  

# np.std() fonksiyonu, bir dizinin standart sapmasını hesaplar. Standart sapma, bir veri setindeki değerlerin ortalamadan ne kadar uzaklaştığını ölçen bir istatistiksel ölçüdür.



 


