import pandas as pd

class Eprofile:
    def __init__(self,name,surname,id,address,location,gender):
        self.name = name
        self.surname = surname
        self.id = id
        self.address = address
        self.location = location
        self.gender = gender

class Rprofile:
    def __init__(self,name,surname,id,address,location,gender):
        self.name = name
        self.surname = surname
        self.id = id
        self.address = address
        self.location = location
        self.gender = gender

E1 = Eprofile ("Ofentse","Mekgwe",9407035261088,"275 Makgotlhane Luka","google_maps","Male")
E2 = Eprofile ("Ofentse","Mekgwe",9407035261088,"275 Makgotlhane Luka","google_maps","Male")
E3 = Eprofile ("Ofentse","Mekgwe",9407035261088,"275 Makgotlhane Luka","google_maps","Male")
Edata =  {
    "Name  ":[E1.name,E2.name,E3.name],
    "Surname":[E1.surname,E2.surname,E3.surname],
    "ID   ":[E1.id,E2.id,E3.id],
    "Address":[E1.address,E2.address,E3.address],
    "Location":[E1.location,E2.location,E3.location],
    "Gender":[E1.gender,E2.gender,E3.gender]
}

Edata2 = pd.DataFrame(Edata)
print(Edata2)
Edata2.to_csv("info")


