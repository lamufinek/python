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


director.init(width=600,height=600, caption = "gra")

director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)

scena = cocos.scene.Scene()


director.run(scena)
