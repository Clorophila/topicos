class Televisor:
    def __init__(self):
        self.volume = 50
        self.canal = 2

    def aumentarVolume(self):
        self.volume += 1
    
    def reduzirVolume(self):
        self.volume -= 1
    
    def trocarCanal(self, canal):
        self.canal = canal

tv = Televisor()
print(tv.canal)
print(tv.volume)

tv.aumentarVolume()
print(tv.volume)

tv.reduzirVolume()
print(tv.volume)

tv.trocarCanal(10)
print(tv.canal)