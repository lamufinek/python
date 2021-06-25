from __future__ import division
from random import *

from cocos.actions import Move
from pyglet.window import key
import cocos.collision_model as cm


import cocos
import resources
import pyglet

from pyglet.window import key


class enemy():
    def __init__(self,x,image):
        self.sprite = cocos.sprite.Sprite(image)
        self.sprite.position = x, 700
        self.sprite.scale = 2
        self.time = 0
        self.canMove = True
        self.sprite.cshape = cm.AARectShape(
            self.sprite.position,
            self.sprite.width/2,
            self.sprite.height/2
        )

    def motion(self,number):
        self.colorTimer()
        self.setColor()
        if(self.canMove):
            accPosition = self.sprite.position
            x = accPosition[0]
            y = accPosition[1] - 4 - randint(1,3)
            self.sprite.position = x,y
            if(y<0):
                self.sprite.position = randint(50,750), 700
                number = number - 1
            self.sprite.cshape.center = self.sprite.position
        return number

    def returnSprite(self):
        return self.sprite

    def hitted(self):
        self.time = 5

    def colorTimer(self):
        self.time = self.time - 1

    def setColor(self):
        if(self.time>0):
            self.sprite.color = (255,30,30)
            self.canMove = False
        elif(self.time == 0):
            self.sprite.position = randint(50,750), 700
        else:
            self.sprite.color = (255,255,255)
            self.canMove = True


        
        





class bullet():
    def __init__(self,position,image):
        self.sprite = cocos.sprite.Sprite(image)
        self.sprite.position = position
        self.sprite.rotation = 180
        self.lifeTime = 120
        self.terminate = False
        self.sprite.cshape = cm.AARectShape(
            self.sprite.position,
            self.sprite.width/2,
            self.sprite.height/2
        )



    def returnSprite(self):
        return self.sprite


    def motion(self):
        accPosition = self.sprite.position
        x = accPosition[0]
        y = accPosition[1] + 6
        self.sprite.position = x,y
        self.sprite.cshape.center = self.sprite.position


    def timer(self):
        self.lifeTime = self.lifeTime - 1
        if(self.lifeTime<0):
            self.terminate = True

        if(self.lifeTime<20):
            self.sprite.scale = 3

    def hitting(self):
        self.lifeTime = 5



class bulletModified():
    def __init__(self,position,image):
        self.modifierX = randint(-10,10)
        self.sprite = cocos.sprite.Sprite(image)
        self.sprite.scale = 2
        self.sprite.position = position
        self.sprite.rotation = 180
        self.lifeTime = 120
        self.terminate = False
        self.sprite.cshape = cm.AARectShape(
            self.sprite.position,
            self.sprite.width/2,
            self.sprite.height/2
        )



    def returnSprite(self):
        return self.sprite


    def motion(self):
        accPosition = self.sprite.position
        x = accPosition[0] + self.modifierX
        y = accPosition[1] + 10
        self.sprite.position = x,y
        self.sprite.cshape.center = self.sprite.position


    def timer(self):
        self.lifeTime = self.lifeTime - 1
        if(self.lifeTime<0):
            self.terminate = True

        if(self.lifeTime<20):
            self.sprite.scale = 3

    def hitting(self):
        self.lifeTime = 5


    







class Game(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super(Game,self).__init__(202, 202, 125, 155)
        self.collision_manager = cm.CollisionManagerBruteForce()
        self.image = pyglet.image.load("resources/sprite.png")
        self.fireballImage = pyglet.image.load("resources/fireball.png")
        self.wolfImage = pyglet.image.load("resources/wolf.png")
        
        self.image_grid = pyglet.image.ImageGrid(self.image, 8,10,item_width=120, item_height =130)
        self.image_grid2 = pyglet.image.ImageGrid(self.wolfImage, 6,20,item_width=32, item_height =64)

        self.walkingWolf = pyglet.image.Animation.from_image_sequence(self.image_grid2[40:45], 0.1, True)
        self.wolfKnockout = pyglet.image.Animation.from_image_sequence(self.image_grid2[66:70], 0.1, True)
        

        self.image_grid_fireball = pyglet.image.ImageGrid(self.fireballImage, 8,8,item_width=64, item_height =64)
        self.fireballAnimation = pyglet.image.Animation.from_image_sequence(self.image_grid_fireball[8:16], 0.1, True)

        self.animationStop = pyglet.image.Animation.from_image_sequence(self.image_grid[10:11], 0.1, True)
        self.animationUp = pyglet.image.Animation.from_image_sequence(self.image_grid[10:20], 0.1, True)
        self.animationDown = pyglet.image.Animation.from_image_sequence(self.image_grid[30:40], 0.1, True)
        self.animationRight = pyglet.image.Animation.from_image_sequence(self.image_grid[0:10], 0.1, True)
        self.animationLeft = pyglet.image.Animation.from_image_sequence(self.image_grid[20:30], 0.1, True)


        self.player = cocos.sprite.Sprite(self.animationStop)

        self.kierunek = "left"

        self.bullets = []

        self.player.position = 400, 100
        self.player.velocity = 0, 0
        self.player.speed =500

        self.wolves = []

        for i in range(5):
            wilk = enemy(randint(50,750),self.walkingWolf)
            super().add(wilk.returnSprite())
            self.collision_manager.add(wilk.returnSprite)
            self.wolves.append(wilk)

        super().add(self.player)

        self.player.do(Move())
        self.schedule(self.update)
        self.lives = 10
        self.motion = True
        self.points = 0

        self.labelPoints = cocos.text.Label(str(self.points), font_size = 32, font_name = "Comic Sans", color = (255,20,147,100))
        self.labelLives = cocos.text.Label(str(self.lives), font_size = 32, font_name = "Comic Sans", color = (25,255,25,100))

        self.naszaEtykieta = cocos.text.Label("Antek",
                                              font_size = 20,
                                              font_name = "Comic Sans",
                                              color = (25,255,25,30))

        self.naszaEtykieta.position = 0,400
        super().add(self.naszaEtykieta)
        
        self.labelPoints.position = 700,600
        self.labelLives.position = 50,600

        super().add(self.labelPoints)
        super().add(self.labelLives)

        self.canGo = True

        

       

    def update(self, dt):
        self.labelLives.element.text = str(self.lives)
        for wilk in self.wolves:
            self.lives = wilk.motion(self.lives)
            
            
        
        for obj in self.bullets:
            if(self.canGo):
                obj.motion()
            obj.timer()
            if(obj.terminate):
                super().remove(obj.returnSprite())
                self.collision_manager.remove_tricky(obj.returnSprite())
                self.bullets.remove(obj)


        for wilk in self.wolves:
            for bullet in self.bullets:
                zmienna = self.collision_manager.they_collide(wilk.returnSprite(),bullet.returnSprite())
                if(zmienna):
                    wilk.hitted()
                    self.points = self.points + 1
                    self.labelPoints.element.text = str(self.points)
                    bullet.hitting()
                    super().remove(bullet.returnSprite())
                    #pos= bullet.returnSprite().position
                    #x = pos[0]
                    #y=  pos[1]
                    self.collision_manager.remove_tricky(bullet.returnSprite())
                    self.bullets.remove(bullet)
                    #tempBullet = bulletModified((x,y), self.fireballAnimation)
                    #super().add(tempBullet.returnSprite())
                    #self.collision_manager.add(tempBullet.returnSprite())
                    #self.bullets.append(tempBullet)
                    self.naszaEtykieta.element.text = self.naszaEtykieta.element.text + "XD!"
                    

       

        
        

    def on_key_press(self, symbol, modifiers):



        if(symbol == key.RIGHT):
            self.player.image = self.animationRight
            self.player.velocity = self.player.speed, 0
            x = self.player.position[0]
            y = self.player.position[1]
            if(x>630):
                x = 630
            self.player.position = x,y 

            self.kierunek = "right"
        elif(symbol == key.LEFT):
            self.player.image = self.animationLeft
            self.player.velocity = -self.player.speed, 0
            self.kierunek = "left"
        elif(symbol == key.SPACE):
            self.shoot()
        elif(symbol == key.B):
            self.fire()

    def on_key_release(self, symbol, modifiers):
        if(symbol == key.LEFT or symbol == key.RIGHT):
            self.player.velocity = 0,0
        
            self.player.image = self.animationStop

    def shoot(self):
        tempBullet = bullet(self.player.position, self.fireballAnimation)
        super().add(tempBullet.returnSprite())
        self.collision_manager.add(tempBullet.returnSprite())
        self.bullets.append(tempBullet)

    def fire(self):
        self.canGo = not self.canGo











cocos.director.director.init(
    width=800,
        height=650,
        caption="game with animation"
    )

game_layer = Game()
game_scene = cocos.scene.Scene(game_layer)

cocos.director.director.run(game_scene)
