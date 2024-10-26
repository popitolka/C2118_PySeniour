print("NIGGERS PIDORAS")

class Marker:
    color: str
    thikness: int
    isAvailable: bool
    def __init__(self, color, thikness, isAvailabe = True):
        self.color = color
        self.thikness = thikness
        self.isAvailable = isAvailabe

    def getInfo(self):
        if self.isAvailable:
            print(f'\tcolor-{self.colo}  thk - {self.thikness}')
        else:
             print('\tthis marker is absent in storage')




markerRed = Marker('red', 2)
markerRed.get_info()
markerRed.color = 'black'
markerRed.get_info()

