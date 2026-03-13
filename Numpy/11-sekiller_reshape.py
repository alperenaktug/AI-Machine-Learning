
import numpy as np

dizi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12])
oto = -1

new_array = dizi.reshape(3, 4)
# reshape fonksiyonu, bir dizinin şeklini değiştirmek için kullanılır. Bu örnekte, 1 boyutlu bir dizi 3 satır ve 4 sütundan oluşan 2 boyutlu bir diziye dönüştürülmüştür. reshape fonksiyonuna verilen yeni şekil, orijinal dizinin eleman sayısıyla uyumlu olmalıdır.
print(new_array)

matris = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_matris = matris.reshape(3 , oto)
print(new_matris)