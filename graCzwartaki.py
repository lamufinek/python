from __future__ import division

from cocos.actions import MoveBy
from pyglet.window import key
import cocos.collision_model as cm


import cocos
import pyglet


class Game(cocos.layer.ColorLayer):

    def __init__(self):
        super(Game,self).__init__(0,0,255,255)
        image = pyglet.image.load("bomb.png")
        self.player = cocos.sprite.Sprite(image)
        self.player.position = 400,300
        self.player.scale = 2
        super().add(self.player)

        move1 = MoveBy((50, 50), 1)
        move2 = MoveBy((-50, -50), 1)

        self.player.do(move1+move2+move1)
        





cocos.director.director.init(
    width=800,
        height=650,
        caption="naszaGra!"
    )

game_layer = Game()
naszaScena = cocos.scene.Scene(game_layer)


cocos.director.director.run(naszaScena)
