
class school:

   

    def __init__(self , şube, öğretmen, bölüm, mevcut_öğrenci):
         self.şube = şube
         self.öğretmen = öğretmen
         self.bölüm = bölüm
         self.mevcut_öğrenci = mevcut_öğrenci

    def info_show(self):
        print("-"* 45)
        print("Şube: ", self.şube)
        print("Öğretmen: ", self.öğretmen)
        print("Bölüm: ", self.bölüm)
        print("Mevcut Öğrenci: ", self.mevcut_öğrenci)
    def teacher_name(self):
        print("-"* 45)
        print("Öğretmen Adı: ", self.öğretmen)    
              

create_class = school("11-A", "Ahmet Yılmaz", "Matematik", 30)

create2_class = school("12-B", "Ayşe Demir", "Fizik", 25)

create_class.info_show() 
create2_class.info_show() 
create2_class.teacher_name()

