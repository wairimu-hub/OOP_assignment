#Base class
class Tribe:
    def __init__(self, name, region, language):
        self.name = name
        self.region = region
        self.language = language

    def introduce(self):
        return f"The {self.name} tribe lives mainly in {self.region} and speaks {self.language}."
    

# Subclasses 
class Kikuyu(Tribe):
    pass

class Luo(Tribe):
    pass

class Maasai(Tribe):
    pass

class Luhya(Tribe):
    pass

#Information
kikuyu = Kikuyu("Kikuyu", "Central Kenya", "Gikuyu")
luo = Luo("Luo", "Lake Victoria and Western Kenya", "Dholuo")
maasai = Maasai("Maasai", "Rift Valley", "Maa")
luhya=Luhya("Luhya", "Western Kenya", "Luhya")

print(kikuyu.introduce())
print(luo.introduce())
print(maasai.introduce())
print(luhya.introduce())
