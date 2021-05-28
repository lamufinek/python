# Import statements as usual
from cocos.sprite import Sprite
from cocos.tiles import load
from cocos.mapcolliders import RectMapCollider
from cocos.layer import ScrollingManager, ScrollableLayer, ColorLayer
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import Action, MoveBy, Repeat  #MoveBy, MoveTo, Rotate, Move() ->velocity
from pyglet.window import key
import cocos.collision_model as cm
import pyglet


class bullet():
    def __init__(self, pos):
        self.image = pyglet.image.load("resources/fireball.png")
        image_gride = pyglet.image.ImageGrid(self.image,8,8,item_width=64,item_height=64)
        self.animation=pyglet.image.Animation.from_image_sequence(image_gride[24:32],0.1,True)
        self.sprite = Sprite(self.animation)
        self.sprite.position = pos
        self.sprite.scale = 1
        self.sprite.rotation = 0
        self.liveTime = 120
        self.sprite.cshape = cm.AARectShape(
                        self.sprite.position,
                    self.sprite.width/3,
                self.sprite.height/3
        )


    def returnSprite(self):
        return self.sprite

    def move(self):
        accPosition = self.sprite.position
        x = accPosition[0] + 3
        y = accPosition[1] 
        self.sprite.position = x,y
        self.sprite.cshape.center = self.sprite.position

    def timer(self):
        self.liveTime = self.liveTime - 1

    def terminator(self):
        if(self.liveTime<0):
            return True




# For this scene, we'll be using a map with a high rectangular block that we don't want the player to be able to pass

# Just as before, I start by initializing the director
director.init(width=700, height=500, autoscale=False, resizable=True)
# This is because, as stated before, many other objects depend on the director being initialized

# And, one again, we set the keyboard and scrolling managers
scroller = ScrollingManager()
keyboard = key.KeyStateHandler()

# I'll also throw in the line that pushes Cocos's handlers to the keyboard object
director.window.push_handlers(keyboard)


mapLayer = load("mapa.tmx")["platformy"]


# This time we'll make an action that extends both the Action class and the new RectMapCollider
# The RectMapCollider, you guessed it, lets us collide with rectmaps (A.K.A. tilemaps)
class GameAction(Action, RectMapCollider):
    # To begin, we'll add a function for when the Action starts
    # I use the start function instead of an __init__ function because of the way the Action parent class is structured
    def start(self):
        # We simply set the velocity of the target sprite to zero
        self.target.velocity = 0, 0

        # We also tell the game that our sprite is starting on the ground
        self.on_ground = True
    def on_bump_handler(self, vx, vy):
        return (vx, vy)

    # Now once again we update this "step" function
    def step(self, dt):
        # To begin we get the delta x and delta y values by grabbing the appropriate parts of the target's velocity
        dx = self.target.velocity[0]
        dy = self.target.velocity[1]

        # Now we make the delta x value equal to the amount left or right they are telling their sprite to move
        dx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 250 * dt
        # This is almost the same as before - once again I combine the left and right values and amplify it so it's visible

        # Here I do the opposite of that "gravity" code I wrote before
        # If the player is on the ground and they hit space...
        if self.on_ground and keyboard[key.SPACE]:
            # they jump into the air the amount that the gravity pulls down
            dy = 6000

        # What we do here may seem a bit odd, but it essentially acts as gravity for the target
        dy -= 4000 * dt
        # I subtract a number, in this case I chose 1500, from the delta y to make it come back down to the floor of the map

        # Here is all of the code for the collision of the target
        # What we do is get a "bounding rectangle", or the imaginary box around the sprite, from the last frame
        last_rect = self.target.get_rect()

        # Then we copy it into a new bounding rectangle that we can alter the values of to match what our math has done
        new_rect = last_rect.copy()

        # So we simply add our new X value to the old one (if it's moving left it will subtract instead)
        new_rect.x += dx

        # And we add our new Y value to the old one as well!
        new_rect.y += (dy * dt)

        # Now we need to actually check for collisions
        #self.target.velocity = self.collide_map(map_layer, last_rect, new_rect, dy, dx)
        self.target.velocity = self.collide_map(mapLayer, last_rect, new_rect, dy, dx)
        # What this line does is run the collide_map function from RectMapCollider to figure out new dx and dy values
        # Then it sets the target's velocity equal to those new dx and dy values

        # Here we check if it is on the ground by looking at the previous bounding rect's y and the current one's y
        # If they're both the same, we know that the target has not moved off the ground!
        self.on_ground = bool(new_rect.y == last_rect.y)

        # Now we need to anchor the position of the target to the middle of the bounding rectangle (or else the target won't move)
        self.target.position = new_rect.center

        # And lastly we set the focus of the scroller to the center of the player (which is the center of the rect)
        scroller.set_focus(*new_rect.center) # The * sets the argument passed in as all of the required parameters
        #scroller.set_focus(new_rect.center[0], 300, force=True)

# Now, once again, we make another class for the sprite's layer
# Remember that it must be a ScrollableLayer

# The first thing we do in our "main" code is make the layer we just defined



class Enemy():
    def __init__(self,x,y,deltaX,deltaY,t):
        image = pyglet.image.load("resources/bat1.png")
        image_gride = pyglet.image.ImageGrid(image,4,4,item_width=32,item_height=32)
        self.animation = pyglet.image.Animation.from_image_sequence(image_gride[13:17],0.1,True)
        self.sprite = Sprite(self.animation)
        self.sprite.position = x,y
        przemieszczenie1 = deltaX,deltaY
        przemieszczenie2 = -deltaX,-deltaY

        ruch = MoveBy(przemieszczenie1,t)+MoveBy(przemieszczenie2,t)

        self.sprite.do(ruch)

    def returnSprite(self):
        return self.sprite

    


class SpriteLayer(ScrollableLayer):
    is_event_handler = True

    def __init__(self):

        super(SpriteLayer,self).__init__()
        image = pyglet.image.load("resources/sprite.png")
        self.collision_manager = cm.CollisionManagerBruteForce()
        self.direction = "right"

        self.bullets = []
        image_gride = pyglet.image.ImageGrid(image,8,10,item_width=120,item_height=130)
        self.animationRight=pyglet.image.Animation.from_image_sequence(image_gride[0:10],0.1,True)
        self.animationLeft=pyglet.image.Animation.from_image_sequence(image_gride[20:30],0.1,True)


        self.sprite = Sprite(self.animationRight)

        enemy = Enemy(400,400,0,0,1)

        super().add(enemy.returnSprite())
        super().add(self.sprite)
        self.sprite.do(GameAction())
        self.schedule(self.update)
        


    def update(self,dt):
        
       
        for obj in self.bullets:
            obj.move()
            obj.timer()
            if(obj.terminator()):
                super().remove(obj.returnSprite())
                self.collision_manager.remove_tricky(obj.returnSprite())
                self.bullets.remove(obj)

    def on_key_press(self, symbol, modifiers):
        if(symbol == key.SPACE):
            self.shoot()
        



    def shoot(self):
        accBullet = bullet(self.sprite.position)
        super().add(accBullet.returnSprite())
        self.collision_manager.add(accBullet.returnSprite())
        self.bullets.append(accBullet)

        


# And lastly I set the position of the sprite to the center of the rectangle


spriteLayer = SpriteLayer()
spriteLayer.sprite.position = 100,300


scroller.add(spriteLayer,z=1)
scroller.add(mapLayer,z=0)


# From here it's pretty easy sailing
# First I add the map, and set the "z" to 0
#scroller.add(map_layer, z=0)
# The z is the vertical axis, so the highest z value layer will always show on top of the others

# Then I add the sprite, and set the z to 1 so that it shows on top of the map layer

bg_color = ColorLayer(52, 152, 219, 1000)

# Then I make a scene
scene = Scene()
# And I add the scroller to it and put it on top of the stack of layers

# And I add the background color (I don't need to define a z because by default it's 0)
scene.add(bg_color)
scene.add(scroller)
# And then we run it!
director.run(scene)
