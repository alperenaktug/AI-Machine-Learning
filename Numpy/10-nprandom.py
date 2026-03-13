
import numpy as np

# 1 ile 10 arasında 5 adet rastgele sayı üretelim

random_numbers = np.random.randint(1, 100, size=5)
# randint fonksiyonu, belirtilen aralıkta (1 dahil, 100 hariç) rastgele tam sayılar üretir. size parametresi ise kaç adet sayı üretileceğini belirtir.
print(random_numbers)

rastgele_numbers = np.random.random(6)*10
# random fonksiyonu, 0 ile 1 arasında rastgele ondalık sayılar üretir.
print(rastgele_numbers)


normal_rakam =  np.random.normal(0,1,5)
# normal fonksiyonu, normal dağılıma (Gaussian dağılımı) göre rastgele sayılar üretir. İlk parametre ortalama (mean), ikinci parametre standart sapma (standard deviation), üçüncü parametre ise kaç adet sayı üretileceğidir.
print(normal_rakam)

rastgele_dizi = np.random.rand(3,3)*10
# rand fonksiyonu, 0 ile 1 arasında rastgele ondalık sayılar üretir. Parametreler ise üretilecek dizinin boyutlarını belirtir.
print(rastgele_dizi)

rasgele_dizi = rastgele_dizi.astype(int)
# astype fonksiyonu, dizinin veri tipini değiştirmek için kullanılır. Bu örnekte, ondalık sayıları tam sayılara dönüştürmek için kullanılmıştır.
