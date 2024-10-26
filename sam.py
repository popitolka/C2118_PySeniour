print('class')

class student:
    name:str
    classname: str
    DZ: int
    isAvailable: bool

    def __init__(self, name, classname, DZ, isAvailable):
        self.name = name
        self.classname = classname
        self.DZ = DZ
        self.isAvailable = isAvailable

    def getInfo(self):
        print('uchenik')
        if self.isAvailable:
            print(f'\tname-{self.name}  - classname - {self.classname} - DZ - {self.DZ} - isAvailable')
        else:
            print('\tprogulivaet')


student1 = student('semen', 'Python', 2)
student1.getInfo()
student2 = ('dania', 'CODU', 5)
student2.getInfo()
