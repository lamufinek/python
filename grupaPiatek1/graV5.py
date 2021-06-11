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


class pocisk():
    def __init__(self, pozycje, kierunek):
        image = pyglet.image.load("resources/fireball.png")
        kawaleczki = pyglet.image.ImageGrid(image,8,8,item_width=64,item_height=64)
        animacja = pyglet.image.Animation.from_image_sequence(kawaleczki[24:32],0.01,True)
        self.pocisk = cocos.sprite.Sprite(animacja)
        self.pocisk.position = pozycje

    def returnSprite(self):
        return self.pocisk



class ourMotion(cocos.actions.Move):

    def step(self,dt):
        super().step(dt)
        vel_x = int(keyboard[key.D]-keyboard[key.A])*300
        vel_y = int(keyboard[key.W]-keyboard[key.S])*300


        self.target.velocity = ( vel_x,vel_y)


class naszaWarstwa(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        self.kierunek = "dół"
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
        if(symbol == key.SPACE):
            bullet = pocisk(self.elf.position, self.kierunek)
            super().add(bullet.returnSprite())

        if(symbol == key.D):
            self.elf.image = self.animacjaPrawo
            self.kierunek = "prawo"

        if(symbol == key.A):
            self.elf.image = self.animacjaLewo
            self.kierunek = "lewo"


        if(symbol == key.W):
            self.elf.image = self.animacjaGora
            self.kierunek = "góra"

        if(symbol == key.S):
            self.elf.image = self.animacjaDol
            self.kierunek = "dół"

        if(symbol == key.P):
            self.elf.scale = self.elf.scale +0.1

        if(symbol == key.O):
            self.elf.scale = self.elf.scale -0.1

    def on_key_release(self, symbol, modifiers):
        self.elf.image = self.animacjaSpoczynek
