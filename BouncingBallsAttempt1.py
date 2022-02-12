import pygame, random, sys, math

WHITE=(255,255,255)

WIDTH = 700
HEIGHT = 500
Size = 23

class Ball:

    def __init__(self, x,y,x_vel,y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel



'''
def make_ball():
    ball = Ball()
    ball.x = random.randrange(Size, WIDTH - Size)
    ball.y = random.randrange(Size, HEIGHT - Size)

    ball.x_vel = random.randrange(-2, 3)
    ball.y_vel = random.randrange(-2, 3)

    return ball
'''

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                sys.exit()

def collide(p1,p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    distance = math.hypot(dx,dy)
    if distance < 2*23: #size:
        p1.x_vel *= -1
        p1.y_vel *= -1
        tangent = math.atan2(dy,dx)
        angle = 0.5*math.pi + tangent
        

pygame.init()

size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing 5 Balls")

run= True

clock = pygame.time.Clock()

#making 5 balls and adding to list
ball_list = []

for i in range(5):
    
    ball = Ball(random.randint(Size, WIDTH - Size),random.randint(Size, HEIGHT - Size),random.randint(-2,5),random.randint(-2,5))
    ball_list.append(ball)

def ball_move():
    for i, ball in enumerate(ball_list):
        ball.x += ball.x_vel
        ball.y += ball.y_vel
        ball.y_vel += 0.09 # gravity

        #bouncing from y co ordinates
        if ball.y > HEIGHT - Size or ball.y < Size:
            ball.y_vel *= -1
            
        # bouncing from x co ordinates
        if ball.x > WIDTH - Size  or ball.x < Size:
            ball.x_vel *= -1

        for ball2 in ball_list[i+1:]:
            collide(ball,ball2)

    

while run:
    quit()

    ball_move()

    

    
    #bg color
    screen.fill((250, 100, 100))

    for ball in ball_list:
        pygame.draw.circle(screen, WHITE, [ball.x, ball.y], Size)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()






