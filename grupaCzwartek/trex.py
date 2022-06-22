import cocos
import pyglet


class Game(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super(Game,self).__init__(202, 202, 125, 155)

        self.image = pyglet.image.load("trex1.png")

        self.player = cocos.sprite.Sprite(self.image)
        self.player.position = 400,400
        self.player.scale = 0.1

        super().add(self.player)




                                    

cocos.director.director.init(
    width=800,
        height=650,
        caption="trex"
    )

game_layer = Game()
game_scene = cocos.scene.Scene(game_layer)

cocos.director.director.run(game_scene)

