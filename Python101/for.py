
# liste = [1, 2, 3, 4, 5]

# for i in liste:
#     print(i)

# for i in range(2, 20 , 2):
#     print(i) 

for i in range(3):
  sifre = input("Lütfen şifrenizi giriniz: ")
  if not sifre:
    print("Şifre boş bırakılamaz.")
  elif len(sifre) in range(3,8):
    print("Yeni şifreniz : " + sifre)  
    break
  elif i == 2:
    print("Şifreyi 3 kere yanlış girdiniz. Hesabınız kilitlendi.")
  else:
    print("Şifre en az 8 karakter olmalıdır. Lütfen tekrar deneyiniz.")   