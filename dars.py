# class Noutbuk():
#     def  __init__(self,protsesor,operativka,a_xotira):
#         self.protsessori = protsesor
#         self.operativkasi = operativka
#         self.asosoy_xotira = a_xotira

#     def get_protsessor(self):
#         return self.protsessori
    
#     def get_oprativkasi(self):
#         return self.operativkasi

#     def get_a_xotira(self):
#         return self.asosoy_xotira
     



#     def info(self):
#         info = f"Protsessori: {self.protsessori}  , Operativkasi: {self.operativkasi}   , Asosiy hotira: {self.asosoy_xotira}"
#         return info

# note = Noutbuk('i5 12gn','ddr4 8gb','512gb ssd')

# print(note.info())




class  Noutbuk():
    def __init__(self,brendi,modeli,protsesor,operativka,a_xotira,ghz,yaderi,potogi):
        self.brendi = brendi
        self.modeli = modeli
        self.protsessori = protsesor
        self.operativkasi = operativka
        self.asosoy_xotira = a_xotira
        self.gerzi = ghz
        self.yaderi = yaderi
        self.potoki = potogi
        

    def get_brendi(self):
        return self.brendi
    
    def get_modeli(self):
        return self.modeli
    
    def get_protsessori(self):
        return self.protsessori
    
    def get_operativkasi(self):
        return self.operativkasi
    

    def get_brendi(self):
        return self.brendi

    def get_brendi(self):
        return self.gerzi
    

    def get_brendi(self):
        return self.yaderi
    
    def get_brendi(self):
        return self.potoki


    

    def set_brendi(self,new_brend ):
        self.brendi=  new_brend
        return self.brendi


    def set_model(self,new_model):
        self.modeli= new_model
        return self.modeli


    def set_protsessori(self,new_protsessor):
        self.protsessori= new_protsessor
        return self.protsessori


    def set_operrativka(self,new_operativka):
        self.operativkasi= new_operativka
        return self.operativkasi


    def set_a_xotira(self,new_asosiy_hotira ):
        self.asosoy_xotira = new_asosiy_hotira
        return self.asosoy_xotira


    def set_ghz(self,new_gerzi):
        self.ghz = new_gerzi
        return self.gerzi


    def set_yader(self,new_yader):
        self.yaderi= new_yader
        return self.yaderi


    def set_potok(self,new_potok):
        self.potoki= new_potok
        return self.potoki


    def info(self):
        info = f"Brendi: {self.brendi}, Modeli: {self.modeli}, Protsesori: {self.protsessori}, Operativka: {self.operativkasi}, Asosiy xotira: {self.asosoy_xotira}, Gerzi: {self.gerzi}, Yaderi: {self.yaderi}, Potoki: {self.potoki}"
        return info



note = Noutbuk('hp','envy x360','i5 12gn','8gb','ssd 512gb','60hz','12','16')

print(note.set_protsessori('amd ryzen 9 16000'))
