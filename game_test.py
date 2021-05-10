import pygame as pg
pg.init()

class Colors:
    def __init__(self, red, green, blue, intensity):
        self._r = red
        self._g = green 
        self._b = blue
        self._intense = intensity 
        
    def intense_colors(self):
        if(self._intense > 3):
            self._intense = 3
        elif(self._intense < 1):
            self._intense = 1
        self._r /= self._intense
        self._g /= self._intense
        self._b /= self._intense
        return (self._r,self._g,self._b)
    
    def get_colors(self):
        return (self._r,self._g,self._b)
        
class Window:
    def __init__(self, wind_x,wind_y):
        self._WINDOW_X = wind_x
        self._WINDOW_Y = wind_y
        self._window_size = (self._WINDOW_X, self._WINDOW_Y)
        pg.display.set_caption("Crossy Roads")
        
    def wind_init(self):
        window_init = pg.display.set_mode(self._window_size)
        return window_init
    def run(self):
        window_active = True
        return window_active
    
class EventHandling:
    def __init__(self, type_event):
        self._type = type_event

class PlayerMovement:
    def __init__(self):
        pass
    
    def get_keys(self):
        keys = pg.key.get_pressed
        return keys()
    
    #def ArrowUp
      #  keys()
x = 50
y = 50 
width = 50
height = 50
player = PlayerMovement().get_keys()
print(player)
'''windw =  Window(800,600)
color = Colors(10,20,50,2)
print(color.get_colors())
status_wind = windw.run()
while(status_wind):
    pg.time.delay(50)
    for event in pg.event.get():
        if(event.type == pg.QUIT):
            status_wind = False
    pg.draw.rect(windw.wind_init(), [0,255,0], [y, x, width, height])
    pg.display.update()'''

pg.quit()