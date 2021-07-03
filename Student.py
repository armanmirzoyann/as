'''

def translate(bar):
    translation = ""
    for tar in bar:
        if tar.upper() in "AEOIU":
            if tar.isupper() :
                translation += "G"
            else:
                translation += "g"
        else:
            translation += tar
    return translation


print(translate(input("Enter the translated text : ")))
'''

class Student:


    def __init__(self,Name,age,year,sallery):
        self.name = Name
        self.age = age
        self.year = year
        self.sallery = sallery
