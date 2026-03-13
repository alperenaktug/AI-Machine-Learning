
# sözlük = {"Apple":"elma" , "Banana":"muz" , "Cherry":"kiraz"}

# print(sözlük["Banana"])


# for i,j in sözlük.items():
#     print(i,":", j)


süper_lig = {"Fenerbahçe": 82, "Galatasaray": 79, "Beşiktaş": 78, "Trabzonspor": 77}

takım = input("Hangi takımın puanını öğrenmek istiyorsunuz? ").capitalize()


print(takım ,":",süper_lig.get(takım, "Bu takım süper ligde yer almıyor."))


