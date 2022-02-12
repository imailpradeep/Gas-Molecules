'''
You can Pause the screen using SPACEBAR

'''
import pygame, sys, random, math
from itertools import combinations

pygame.init()
mainClock = pygame.time.Clock()

pygame.display.set_caption('Gravity Balls using Classes')
SCREEN_Wid, SCREEN_Len = 700,500
screen = pygame.display.set_mode((SCREEN_Wid, SCREEN_Len))



BallsList = []
count = 1
ballcount = 5  #for drawing 5 balls

class MovingBalls():

    gravity = 0.2 #constant value
    
    def __init__(self,x,y,Vx,Vy,color,size):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.color = color
        self.size = size
        
    def move(self):
        self.x += self.Vx
        self.y += self.Vy
        self.Vy += self.gravity

        if(self.y >= (SCREEN_Len - self.size)):
            self.y = SCREEN_Len-self.size
            self.Vy *= -0.95
            
        if(self.y <= self.size):
            self.y = self.size
            self.Vy *= -0.95
            
        if(self.x >= (SCREEN_Wid - self.size)):
            self.x = SCREEN_Wid-self.size
            self.Vx *= -1
            
        if(self.x <= self.size):
            self.x = self.size
            self.Vx *= -1
            
        pygame.draw.circle(screen, self.color,(round(self.x),round(self.y)), self.size)
        



def paused(): #pause function (with spacebar)
    global pause
    pygame.display.set_caption('I am Paused')
    while pause:
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if(event.type == pygame.KEYDOWN): 
                if(event.key == pygame.K_SPACE):
                    pause = False

                    
# Game Loop
while True:
    screen.fill((255, 255, 255))

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if(event.key == pygame.K_SPACE):
                pause = True
                paused()
                pygame.display.set_caption('Gravity Balls using Classes')

# Background --------------------------------------------- #
        while count <= ballcount: #draw 5 objects(balls)
            randX = random.randint(-5,5)
            while(randX == 0): # ball's x_vel will never get 0
                randX = random.randint(-5,5)
                
            randY = random.randint(-5,5)
            while(randY == 0): # ball's y_vel will never get 0
                randY = random.randint(-5,5)
                
            x= random.randint(50,600)
            y= random.randint(50,400)
            randColor =(random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
            randSize = random.randint(10,30)

            a = MovingBalls(x,y,randX,randY,randColor,randSize)
            BallsList.append(a)

            count += 1

    for ball in BallsList:
      ball.move()
  
    for j,k in combinations(BallsList,2):
        v1 = pygame.math.Vector2(j.x, j.y)
        v2 = pygame.math.Vector2(k.x, k.y)

        if(v2.distance_to(v1) <= 40 ):
            
            diff = v2 - v1
            j.Vx, j.Vy = pygame.math.Vector2(j.Vx,j.Vy).reflect(diff)
            k.Vx, k.Vy = pygame.math.Vector2(k.Vx,k.Vy).reflect(diff)
           

   
 # Update ------------------------------------------------- #
    pygame.display.update()
    
    mainClock.tick(60)
