
import numpy as np 

dize= np.array([10 , 20, 30, 40, 50, 89,76,56,45,23])

# boolmask = dize >= 50
# print(boolmask)

# Boolean Indexing (Boolean İndeksleme) :
# Boolean indexing, bir dizi veya veri setindeki belirli koşullara uyan elemanları seçmek için kullanılan bir tekniktir. Bu yöntem, bir dizi üzerinde koşullu ifadeler kullanarak belirli elemanları filtrelemenize olanak tanır. Boolean indexing, veri analizi ve manipülasyonu sırasında sıklıkla kullanılır, özellikle büyük veri setlerinde belirli kriterlere uyan verileri hızlıca seçmek için faydalıdır.

# secilmiş = dize[boolmask]
# print("50'den büyük olan elemanlar: ", secilmiş)


booleans_mask2 = (dize > 50 ) & (dize < 80)
print("50 den büyük ve 80 den küçük olan elemanlar: ", dize[booleans_mask2])


