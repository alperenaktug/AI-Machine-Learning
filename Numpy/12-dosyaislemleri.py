
import numpy as np

data = np.loadtxt('C:\\Users\\aktug\\OneDrive\\Masaüstü\\data.txt', delimiter=' ')

# print(data)


row_sum = np.sum(data, axis=1)
#axis=1, satırların toplamını hesaplamak için kullanılır. Eğer axis=0 olsaydı, sütunların toplamını hesaplamış olurduk.

# print("Satırların Toplamı:", row_sum) 

output_data = np.column_stack((data, row_sum))
np.savetxt('C:\\Users\\aktug\\OneDrive\\Masaüstü\\output.txt',output_data,  fmt='%d' , delimiter=' ')
print("Çıktı dosyası başarıyla oluşturuldu.")
