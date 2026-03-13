
import numpy as np

dizi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

free = dizi[2]
print(free)  

# dizinin 2. indeksindeki elemanı verir (0 tabanlı indeksleme kullanılır).


matris = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

eleman = matris[0,0]
print(eleman)


# matrisin 0. satır ve 0. sütunundaki elemanı verir (0 tabanlı indeksleme kullanılır).


dilim = dizi[2:5]
print(dilim)

# dizinin 2. indeksinden başlayarak 5. indekse kadar olan elemanları verir (5 dahil değil).

dilim = dizi[5:9]
print(dilim)

# dizinin 2. indeksinden başlayarak 5. indekse kadar olan elemanları verir (5 dahil değil).
