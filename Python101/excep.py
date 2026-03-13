
import time
try:

  sayı1 = int(input("Lütfen 1. sayıyı giriniz:"))
  sayı2 = int(input("Lütfen 2. sayıyı giriniz:"))
  
  print("Sayıların bölümü:", sayı1+sayı2)
  
# except ZeroDivisionError:
#     print("Sayı 0'a bölünemez.")
except ValueError:
    print("Lütfen geçerli bir sayı giriniz.") 

finally:
    sayac = 5
    for sayac in range(5,0,-1):
        time.sleep(0.5)
        print("Geri sayım: " ,sayac)
    print("Program sonlandı.")     




