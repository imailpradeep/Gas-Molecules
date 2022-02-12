# prgram to make particles collide and display conservation of momentum
# import modules
import pygame, sys, random, math

# declare variables
background_colour = (255,100,100)
(width, height) = (400, 400)
drag = 0.999
elasticity = 0.99
gravity = [math.pi, 0.0002]

# STANDARD quit function           
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

# function to add vectors and return the resultant angle and magnitude
def addVectors(angle1, length1, angle2, length2):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2 # x is sine due to convention up is 0 and down in pi
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2 # angle from positive y axis clockwise
    
    angle = 0.5 * math.pi - math.atan2(y, x) # because of convention in pygame total angle is pi/2 and we remove the angle 
    length  = math.hypot(x, y)
    
    return angle, length
    

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors(p1.angle, p1.speed*(p1.mass-p2.mass)/total_mass, angle, 1.9*p2.speed*p2.mass/total_mass)
        (p2.angle, p2.speed) = addVectors(p2.angle, p2.speed*(p2.mass-p1.mass)/total_mass, angle+math.pi, 1.9*p1.speed*p1.mass/total_mass)

        overlap = 0.5*(p1.size + p2.size - dist)
        p1.x += math.sin(angle)*overlap
        p1.y -= math.cos(angle)*overlap
        p2.x -= math.sin(angle)*overlap
        p2.y += math.cos(angle)*overlap

class Particle():
    def __init__(self, x, y, size, mass=1):
        self.x = x
        self.y = y
        self.size = size
        self.mass = mass
        self.colour = (0, 0, 255)
        self.thickness = 0
        self.speed = 0
        self.angle = 0
              
# draw circle on screen
    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
# calculate movement, the gravity is one vector and velocity is another hmmm...
    def move(self):
        self.angle, self.speed = addVectors(self.angle, self.speed, math.pi, 0.0002) #gravity = math.pi, 0.0002
        
        self.x += (math.sin(self.angle) * self.speed)
        self.y -= (math.cos(self.angle) * self.speed)

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed += (1 - self.speed)*0.2

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed += (1 - self.speed)*0.2

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed += (1 - self.speed)*0.2

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed += (1 - self.speed)*0.2

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Conservation of Momentum')
clock = pygame.time.Clock()
number_of_particles = 10
my_particles = []

for n in range(number_of_particles):
    size = 10

    if n < number_of_particles/2:
        density = random.randint(5, 10)
    else:
        density = random.randint(15, 20)

    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    particle = Particle(x, y, density, density*size**2)# density is given as size
    if n < number_of_particles/2:
        particle.colour = (density*25, 0, 0)
    else:
        particle.colour = (50, 50, density*12)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)

    my_particles.append(particle)

#game loop
selected_particle = None # starts with no selected particles
run = True
while run:

    quit() # option to quit the game
    screen.fill(background_colour) # put background colour

    for i, particle in enumerate(my_particles): # enumerate gives two values as output
        particle.move() # call move function in particle class
        particle.bounce() # call bounce function in particle class
        for particle2 in my_particles[i+1:]: # check for collision with the remaining particles
            collide(particle, particle2) # call collide function
        particle.display() # call display function

    pygame.display.flip() # update display
    clock.tick(200)
