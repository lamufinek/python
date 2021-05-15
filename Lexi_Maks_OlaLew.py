from __future__ import division
from random import *

from cocos.actions import *
#from pyglet.window import *
import cocos.collision_model as cm
from cocos.layer import *

import cocos
from cocos.director import director
from pyglet.window import key
#from cocos import mapcolliders
from cocos.sprite import Sprite
from cocos.tiles import load
from cocos.mapcolliders import RectMapCollider
from cocos.layer import ScrollingManager, ScrollableLayer, ColorLayer
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import Action, MoveTo, Rotate,Repeat  #MoveBy, MoveTo, Rotate, Move() ->velocity
from pyglet.window import key
import pyglet


class ourMotion(cocos.actions.Move):

    def step(self,dt):
        super().step(dt)
        vel_x = int(keyboard[key.D]-keyboard[key.A])*300
        vel_y = int(keyboard[key.W]-keyboard[key.S])*300


        self.target.velocity = ( vel_x,vel_y)


class naszaWarstwa(ColorLayer):
    def __init__(self):
        super().__init__(0,120,120,255)
        aktor = Sprite("superman.png")

        super().add(aktor)
        aktor.position = 300,300
        aktor.scale = 0.1

        #ustawi pozycjÄ   aktor.position = 300,300

        pos1 = 600,600
        ruch1 = MoveTo(pos1,3)

        pos2 = 0,600
        ruch2 = MoveTo(pos2,3)

        ruch3 = ruch1+ruch2

        aktor.do(ruch3)




director.init(width= 800, height = 600)

director.window.pop_handlers()
keyboard = key.KeyStateHandler()
director.window.push_handlers(keyboard)


scena1 = Scene()
scena1.add(naszaWarstwa())


director.run(scena1)
