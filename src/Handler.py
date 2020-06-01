import src.map as map


class Handler:   
    def __init__(self, worldPar):
        self.wPar = worldPar
        self.Map = None

    def create_map(self):
        self.Map = map.Map(self.wPar.WorldSize)
        self.Map.generate()

    def create_world(self):
        self.create_map()
#+ bot and food
        

    def RunOnTick(self):
        '''Готовит изображение для вывода'''
