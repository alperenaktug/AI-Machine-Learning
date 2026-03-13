
import numpy as np

dizi = np.array([1, 2, 3, 4, 59])



# Kümülatif Toplam (Cumulative Sum) :
# Kümülatif toplam, bir dizi veya veri setindeki her bir elemanın kendisinden önceki elemanların toplamını içeren yeni bir dizi oluşturur. Bu, her bir elemanın kendisinden önceki tüm elemanların toplamını gösterir. Kümülatif toplam, veri analizi ve istatistikte sıklıkla kullanılır, özellikle zaman serisi verilerinde trendleri ve değişimleri anlamak için faydalıdır.

kume_toplam = np.cumsum(dizi)
print("Küme Toplamı: ", kume_toplam)