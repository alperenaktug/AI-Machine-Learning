
# sayı = 0

# while sayı <=10:
#    print(sayı)
#    sayı += 2


db_username = "admin"
db_password = 1579

while True:
  username = input("Kullanıcı adınızı giriniz: ")
  password = int(input("Şifrenizi giriniz: "))

  if username == db_username and password == db_password:
    print("Giriş başarılı!")
    break
  elif username != db_username and password == db_password:
    print("Kullanıcı adınız yanlış.")
    
  elif username == db_username and password != db_password:
    print("Şifreniz yanlış.")
    print(input("Şifrenizi değiştirmek ister misiniz ? (E/H)")) 
    cevap = input()
    if cevap == "E":
      print("Şifrenizi değiştirmek için lütfen yeni şifrenizi giriniz:")
      new_password = int(input("Yeni şifrenizi giriniz: ")) 
      db_password = new_password
      print("Şifreniz başarıyla değiştirildi.")
  else:
      print("Kullanıcı adı ve şifreniz hatalı .")   
      
