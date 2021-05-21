from __future__ import division
from random import *

from cocos.actions import *
#from pyglet.window import *
import cocos.collision_model as cm


import cocos
import pyglet
from cocos.director import director
from pyglet.window import key
#from cocos import mapcolliders


class ourMotion(cocos.actions.Move):

    def step(self,dt):
        super().step(dt)
        vel_x = int(keyboard[key.D]-keyboard[key.A])*300
        vel_y = int(keyboard[key.W]-keyboard[key.S])*300


        self.target.velocity = ( vel_x,vel_y)


class naszaWarstwa(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__(0,0,255,180)
        image = pyglet.image.load("resources/sprite.png")
        self.jakiRuch = "spoczynek"

        kawaleczki = pyglet.image.ImageGrid(image,8,10,item_width=120,item_height=130)

        self.animacjaPrawo = pyglet.image.Animation.from_image_sequence(kawaleczki[0:9],0.01,True)
        self.animacjaLewo = pyglet.image.Animation.from_image_sequence(kawaleczki[20:29],0.01,True)
        self.animacjaGora = pyglet.image.Animation.from_image_sequence(kawaleczki[10:19],0.01,True)
        self.animacjaDol = pyglet.image.Animation.from_image_sequence(kawaleczki[30:39],0.01,True)
        self.animacjaSpoczynek = pyglet.image.Animation.from_image_sequence(kawaleczki[70:73],0.1,True)



        self.elf = cocos.sprite.Sprite(self.animacjaSpoczynek)
        self.elf.position = 300,300
        self.elf.velocity = 0,0
        self.elf.do(ourMotion())
        super().add(self.elf) 
        #self.schedule(self.update)

    def on_key_press(self, symbol, modifiers):

        if(symbol == key.D):
            self.elf.image = self.animacjaPrawo

        if(symbol == key.A):
            self.elf.image = self.animacjaLewo

        if(symbol == key.W):
            self.elf.image = self.animacjaGora

        if(symbol == key.S):
            self.elf.image = self.animacjaDol

    def on_key_release(self, symbol, modifiers):
        self.elf.image = self.animacjaSpoczynek


        


director.init(width=600,height=600, caption = "gra")

director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)

scena = cocos.scene.Scene()
scena.add(naszaWarstwa())

director.run(scena)
