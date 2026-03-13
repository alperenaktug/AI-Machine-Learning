
import numpy as np

dizi = np.array([["Pazartesi" ,"Salı", "Çarşamba" , "Perşembe" , "Cuma"], [6, 7, 8, 9, 10]])


print(dizi.shape)
# Bir dizinin boyutunu öğrenmek için shape özelliğini kullandık ve sonucu ekrana yazdırdık. Bu dizi 2 satır ve 5 sütundan oluştuğu için (2, 5) şeklinde bir çıktı verecektir.

dizi2 = np.array([[[1,2,3], [4, 5 ,6] , [7,8,9] ]])

print(dizi2.shape)
# Bu dizi 1 blok, 3 satır ve 3 sütundan oluştuğu için (1, 3, 3) şeklinde bir çıktı verecektir. shape özelliği, dizinin her bir boyutunun uzunluğunu gösterir.