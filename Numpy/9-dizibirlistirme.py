
import numpy as np

# dizi1 = np.array([1,2,3])
# dizi2 = np.array([4,5,6])

# birlesik_dizi = np.concatenate((dizi1, dizi2))
# print("Birleştirilmiş Dizi :",birlesik_dizi)


# İKİ BOYUTLU DİZİLERİ BİRLEŞTİRME

# İki boyutlu dizileri birleştirmek için NumPy'da birkaç farklı yöntem vardır. En yaygın kullanılan yöntemler arasında `hstack` (yatay birleştirme) ve `vstack` (dikey birleştirme) bulunur.

# dizi1 = np.array([[1,2,3], [4,5,6]])
# dizi2 = np.array([[7,8,9], [10,11,12]])

# birlestir_dizi = np.hstack((dizi1, dizi2))
# print("*" * 25)
# birlestir_dizi2 = np.vstack((dizi1, dizi2))

# print("Yatay Birleştirilmiş Dizi :\n", birlestir_dizi)
# print ("Dikey Birleştirilmiş Dizi :\n", birlestir_dizi2)

# DİZİLERDE BÖLME İŞLEMLERİ

# Dizi bölme işlemi, bir diziyi belirli bir boyutta veya belirli bir kritere göre parçalara ayırmak anlamına gelir. NumPy'da dizi bölme işlemi için birkaç farklı yöntem bulunmaktadır. En yaygın kullanılan yöntemler arasında `split`, `array_split`, `hsplit` ve `vsplit` bulunur.


# dizi_bolme = np.array([1,2,3,4,5,6,7,8,9])

# bolme = np.split(dizi_bolme, 3)
# print("Dizi Bölme İşlemi : ", bolme)

dizi_bolme2 = np.array([[1,2,3,4],[5,6,7,8]])

bolme1 = np.hsplit(dizi_bolme2, 2)
print("*" * 25)
bolme2 = np.vsplit(dizi_bolme2, 2)

print("Dikey Bölme İşlemi : ", bolme1)
print("Yatay Bölme İşlemi : ", bolme2)



