
import numpy as np

dizi1 = np.array([1, 2, 3, 4, 5])
dizi2 = np.array([6,34,19,45,7])

topla = np.add(dizi1, dizi2) 
fark = np.subtract(dizi1, dizi2)
carpma = np.multiply(dizi1, dizi2)  
bolme = np.divide(dizi1, dizi2)


print("Toplama İşlemi Sonucu: ", topla)
print("Çıkarma İşlemi Sonucu: ", fark)
print("Çarpma İşlemi Sonucu: ", carpma)
print("Bölme İşlemi Sonucu: ", bolme)

 # Üs Alma İşlemi : 

üst = np.power(dizi1, 2)
print("Dizi1'in Üssü:", üst)

# Kök Alma İşlemi :

kök = np.sqrt(dizi2)
print("Dizi2'nin Kökü:", kök)


# Varyans Nedir ? 
# Varyans, bir veri setindeki değerlerin ortalamadan ne kadar uzaklaştığını ölçen bir istatistiksel kavramdır. Yüksek varyans, verilerin ortalamadan daha fazla uzaklaştığını gösterirken, düşük varyans, verilerin ortalamaya daha yakın olduğunu gösterir. Varyans, genellikle veri setinin dağılımını anlamak ve karşılaştırmak için kullanılır.

varyans = np.var(dizi1)
varyans2 = np.var(dizi2)
print("Dizi1'in Varyansı: ", varyans)
print("Dizi2'nin Varyansı: ", varyans2)
