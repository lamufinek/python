from __future__ import division

from cocos.actions import Move
from pyglet.window import key
import cocos.collision_model as cm


import cocos
import resources
import pyglet

from pyglet.window import key
from cocos.actions import MoveBy
from cocos.actions import Place


class segment():
    def __init__(self,x,y):
        self.graphics = pyglet.image.load("resources/wall.jpg")
        self.mySprite = cocos.sprite.Sprite(self.graphics)
        self.mySprite.position = x,y
        self.mySprite.scale = 0.05

    def returnSprite(self):
        return self.mySprite


class wall():
    def __init__(self,xStart,yStart,xFinish,yFinish):
        if(xStart<xFinish):
            xIncrease = "yes"
        elif(xStart>xFinish):
            xIncrease = "no"
        else:
            xIncrease = "constant"

        if(yStart<yFinish):
            yIncrease = "yes"
        elif(yStart>yFinish):
            yIncrease = "no"
        else:
            yIncrease = "constant"

        xLenght = abs(xStart-xFinish)
        yLenght = abs(yStart-yFinish)
        self.brics = []
        if(xLenght>yLenght):
            iterator = xLenght/52
        else:
            iterator = yLenght/52
        for i in range(int(iterator)):
            if(xIncrease=="yes"):
                x = xStart + i*xLenght/iterator
            elif(xIncrease=="no"):
                x = xStart - i*xLenght/iterator
            else:
                x = xStart


            if(yIncrease=="yes"):
                y = yStart + i*yLenght/iterator
            elif(yIncrease=="no"):
                y = yStart - i*yLenght/iterator
            else:
                y = yStart
            duch = segment(x,y).returnSprite()
            self.brics.append(duch)

    def returnWall(self):
        return self.brics



class mapWalls():
    def __init__(self,collision_manager):
        positions = []
        self.batch = cocos.batch.BatchNode()
        self.mapWalls = []
        for i in range(int(len(positions)/4)):
            tablica = (wall(positions[i*4],positions[i*4+1],positions[i*4+2],positions[i*4+3]).returnWall())
            for obj in tablica:
                obj.cshape = cm.AARectShape(
                obj.position,
                obj.width/2,
                obj.height/2)
                collision_manager.add(obj)
                self.batch.add(obj)
                self.mapWalls.append(obj)


    def returnMapWallsBatch(self):
        return self.batch

    def returnMapWalls(self):
        return self.mapWalls









class Game(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super(Game,self).__init__(202, 202, 125, 155)
        self.collision_manager = cm.CollisionManagerBruteForce()
        self.collision_manager.enabled = True
        self.collision_manager.enabledDrawBoundingBox = True;
        img = pyglet.image.load("resources/sprite.png")
        self.img2= pyglet.image.load("resources/fireball.png")
        self.bullets = []
        self.kierunek = "Right"
        self.img_grid = pyglet.image.ImageGrid(img, 8,10, item_width = 120, item_height=130)
        self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[50:51], 1/150 , True)
        self.animWalkUp = pyglet.image.Animation.from_image_sequence(self.img_grid[10:20], 1/15 , True)
        self.animWalkDown = pyglet.image.Animation.from_image_sequence(self.img_grid[30:40], 1/15 , True)
        self.animWalkRight = pyglet.image.Animation.from_image_sequence(self.img_grid[0:10], 1/15 , True)
        self.animWalkLeft = pyglet.image.Animation.from_image_sequence(self.img_grid[20:30], 1/15 , True)
        self.leftPressed = False
        self.righPressed = False
        self.upPressed   = False
        self.downPressed = False
        self.spacePressed= False
        self.keysPressed = []
        self.keysPressed.append(None)
        self.keysPressed.append(None)
        self.keysPressed.append(None)
        self.player = cocos.sprite.Sprite(self.anim)
        self.player.position = 400, 225
        self.player.velocity = 0, 0
        self.player.speed =150
        self.player.scale = 0.2
        self.player.cshape = cm.AARectShape(
            self.player.position,
            self.player.width/2,
            self.player.height/2
        )

        super().add(self.player)
        self.collision_manager.add(self.player)
        super().add(self.player)

        #super().add(mapWalls().returnMapWalls())
        self.mapWalls= mapWalls(self.collision_manager)
        self.wallsColliding = self.mapWalls.returnMapWalls()
        for obj in self.wallsColliding:
            self.collision_manager.add(obj)
        super().add(self.mapWalls.returnMapWallsBatch())


        #self.collision_manager.add(self.mapWalls
        self.licznik = 0
        self.player.do(Move())
        self.schedule(self.update)
#        self.schedule(self.update)

    def update(self,dt):
        self.player.cshape.center = self.player.position
        collidingWithPlayer = self.collision_manager.objs_colliding(self.player)
        if(collidingWithPlayer):
            for obj in self.wallsColliding:
                if(obj in collidingWithPlayer):
                    self.licznik = self.licznik + 1
                    self.playerBack()
                    self.player.do(Move())


    def playerBack(self):
        if(self.player.velocity[0]>0):
            x = self.player.position[0]-10
            y= self.player.position[1]
            self.player.do( Place( (x, y) ))

    def on_key_press(self, symbol, modifiers):



        if symbol == key.SPACE:
            self.player.speed = 500
            self.animWalkUp = pyglet.image.Animation.from_image_sequence(self.img_grid[10:20], 1/(self.player.speed/10) , True)
            self.animWalkDown = pyglet.image.Animation.from_image_sequence(self.img_grid[30:40], 1/(self.player.speed/10) , True)
            self.animWalkRight = pyglet.image.Animation.from_image_sequence(self.img_grid[0:10], 1/(self.player.speed/10) , True)
            self.animWalkLeft = pyglet.image.Animation.from_image_sequence(self.img_grid[20:30], 1/(self.player.speed/10) , True)



        if symbol == key.LEFT:
            self.keysPressed[2] = self.keysPressed[1]
            self.keysPressed[1] = self.keysPressed[0]
            self.keysPressed[0] ="Left"
        elif symbol == key.RIGHT:
            self.keysPressed[2] = self.keysPressed[1]
            self.keysPressed[1] = self.keysPressed[0]
            self.keysPressed[0] ="Right"
        elif symbol == key.UP:
            self.keysPressed[2] = self.keysPressed[1]
            self.keysPressed[1] = self.keysPressed[0]
            self.keysPressed[0] ="Up"
        elif symbol == key.DOWN:
            self.keysPressed[2] = self.keysPressed[1]
            self.keysPressed[1] = self.keysPressed[0]
            self.keysPressed[0] ="Down"


        keyOne = self.keysPressed[0]
        keyTwo = self.keysPressed[1]

        if(keyOne == "Left" and keyTwo == "Right"):
            self.player.velocity = (-self.player.speed, 0)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Right" and keyTwo == "Left"):
            self.player.velocity = (self.player.speed, 0)
            self.player.image = self.animWalkRight
        elif(keyOne == "Left" and keyTwo == None):
            self.player.velocity = (-self.player.speed, 0)
            self.player.image = self.animWalkLeft
        elif(keyOne == None and keyTwo == "Left"):
            self.player.velocity = (-self.player.speed, 0)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Right" and keyTwo == None):
            self.player.velocity = (self.player.speed, 0)
            self.player.image = self.animWalkRight
        elif(keyOne == None and keyTwo == "Right"):
            self.player.velocity = (self.player.speed, 0)
            self.player.image = self.animWalkRight
        elif(keyOne == "Up" and keyTwo == "Right"):
            self.player.velocity = (self.player.speed, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Right" and keyTwo == "Up"):
            self.player.velocity = (self.player.speed, self.player.speed)
            self.player.image = self.animWalkRight
        elif(keyOne == "Up" and keyTwo == None):
            self.player.velocity = (0, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == None and keyTwo == "Up"):
            self.player.velocity = (0, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Up" and keyTwo == "Left"):
            self.player.velocity = (-self.player.speed, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Left" and keyTwo == "Up"):
            self.player.velocity = (-self.player.speed, self.player.speed)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Down" and keyTwo == "Right"):
            self.player.velocity = (self.player.speed, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == "Right" and keyTwo == "Down"):
            self.player.velocity = (self.player.speed, -self.player.speed)
            self.player.image = self.animWalkRight
        elif(keyOne == "Down" and keyTwo == "Left"):
            self.player.velocity = (-self.player.speed, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == None and keyTwo == "Down"):
            self.player.velocity = (0, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == "Down" and keyTwo == None):
            self.player.velocity = (0, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == "Left" and keyTwo == "Down"):
            self.player.velocity = (-self.player.speed, -self.player.speed)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Up" and keyTwo == "Down"):
            self.player.velocity = (0,self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Down" and keyTwo == "Up"):
            self.player.velocity = (0,-self.player.speed)
            self.player.image = self.animWalkDown
        else:
            self.player.velocity = (0,0)
            self.player.image = self.anim





    def on_key_release(self, symbol, modifiers):

        if symbol == key.SPACE:
            self.player.speed = 150
            self.animWalkUp = pyglet.image.Animation.from_image_sequence(self.img_grid[10:20], 1/(self.player.speed/10) , True)
            self.animWalkDown = pyglet.image.Animation.from_image_sequence(self.img_grid[30:40], 1/(self.player.speed/10) , True)
            self.animWalkRight = pyglet.image.Animation.from_image_sequence(self.img_grid[0:10], 1/(self.player.speed/10) , True)
            self.animWalkLeft = pyglet.image.Animation.from_image_sequence(self.img_grid[20:30], 1/(self.player.speed/10) , True)

        if symbol == key.O:
            self.shoot()
        if symbol == key.P:
            self.remove()

        if(symbol == key.RIGHT):
            if self.keysPressed[0] == "Right":
                self.keysPressed[0]= None
            if self.keysPressed[1] == "Right":
                self.keysPressed[1]= None

        if(symbol == key.LEFT):
            if self.keysPressed[0] == "Left":
                self.keysPressed[0]= None
            if self.keysPressed[1] == "Left":
                self.keysPressed[1]= None

        if(symbol == key.UP):
            if self.keysPressed[0] == "Up":
                self.keysPressed[0]= None
            if self.keysPressed[1] == "Up":
                self.keysPressed[1]= None

        if(symbol == key.DOWN):
            if self.keysPressed[0] == "Down":
                self.keysPressed[0]= None
            if self.keysPressed[1] == "Down":
                self.keysPressed[1]= None



        keyOne = self.keysPressed[0]
        keyTwo = self.keysPressed[1]

        if(keyOne == "Left" and keyTwo == "Right"):
            self.player.velocity = (-self.player.speed, 0)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Right" and keyTwo == "Left"):
            self.player.velocity = (self.player.speed, 0)
            self.player.image = self.animWalkRight
        elif(keyOne == "Left" and keyTwo == None):
            self.player.velocity = (-self.player.speed, 0)
            self.player.image = self.animWalkLeft
        elif(keyOne == None and keyTwo == "Left"):
            self.player.velocity = (-self.player.speed, 0)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Right" and keyTwo == None):
            self.player.velocity = (self.player.speed, 0)
            self.player.image = self.animWalkRight
        elif(keyOne == None and keyTwo == "Right"):
            self.player.velocity = (self.player.speed, 0)
            self.player.image = self.animWalkRight
        elif(keyOne == "Up" and keyTwo == "Right"):
            self.player.velocity = (self.player.speed, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Right" and keyTwo == "Up"):
            self.player.velocity = (self.player.speed, self.player.speed)
            self.player.image = self.animWalkRight
        elif(keyOne == "Up" and keyTwo == None):
            self.player.velocity = (0, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == None and keyTwo == "Up"):
            self.player.velocity = (0, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Up" and keyTwo == "Left"):
            self.player.velocity = (-self.player.speed, self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Left" and keyTwo == "Up"):
            self.player.velocity = (-self.player.speed, self.player.speed)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Down" and keyTwo == "Right"):
            self.player.velocity = (self.player.speed, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == "Right" and keyTwo == "Down"):
            self.player.velocity = (self.player.speed, -self.player.speed)
            self.player.image = self.animWalkRight
        elif(keyOne == "Down" and keyTwo == "Left"):
            self.player.velocity = (-self.player.speed, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == None and keyTwo == "Down"):
            self.player.velocity = (0, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == "Down" and keyTwo == None):
            self.player.velocity = (0, -self.player.speed)
            self.player.image = self.animWalkDown
        elif(keyOne == "Left" and keyTwo == "Down"):
            self.player.velocity = (-self.player.speed, -self.player.speed)
            self.player.image = self.animWalkLeft
        elif(keyOne == "Up" and keyTwo == "Down"):
            self.player.velocity = (0,self.player.speed)
            self.player.image = self.animWalkUp
        elif(keyOne == "Down" and keyTwo == "Up"):
            self.player.velocity = (0,-self.player.speed)
            self.player.image = self.animWalkDown
        else:
            self.player.velocity = (0,0)
            self.player.image = self.anim


    def shoot(self):
        l = len(self.bullets)
        self.bullets.append(cocos.sprite.Sprite(self.img2))
        self.bullets[l].position = self.player.position
        super().add(self.bullets[l])

    def remove(self):
        l = len(self.bullets)
        super().remove(self.bullets[l-1])
                    #elif symbol == key.C:
            #self.anim = pyglet.image.Animation.from_image_sequence(self.img_grid[0:10], 0.05 , True)
            #self.player.image = self.anim

#    def update(self,dt):
#        if(key.RIGHT):
#            velX = (key.RIGHT)*0.005
#            velY = 0
#        elif(key.LEFT):
#            velX = (- key.LEFT)*0.005
#       elif(key.DOWN):
#            velY = (- key.DOWN)*0.005
#            velX = 0
#           velY = (key.UP)*0.005
#            velX = 0
#        else:
#            velX = 0
#            velY = 0
#        self.player.velocity = (velX,velY)





cocos.director.director.init(
    width=800,
        height=650,
        caption="Catch your husband!"
    )

game_layer = Game()
game_scene = cocos.scene.Scene(game_layer)

cocos.director.director.run(game_scene)
