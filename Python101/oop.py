class galeri:
    arac_ismi = "Audi"
    km_Degeri = 100000
    renk = "Sarı"

    def araba_properties(self):
        print("Araba Adı: ", self.arac_ismi)
        print("Araba Km Değeri: ", self.km_Degeri)
        print("Araba Rengi: ", self.renk)


car = galeri()   


car.araba_properties()


print("--- Doğrudan Erişim ---")
print("Araba Adı: ", car.arac_ismi)
print("Araba Km Değeri: ", car.km_Degeri)  
     
