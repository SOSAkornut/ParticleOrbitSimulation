import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Particle Orbit Simulation")


particleX = 0
particleY = 0

ObjectX = 400
ObjectY = 300

def particle(x, y, color, size):
   pygame.draw.circle(screen, color, [x, y], size)

def Object(x, y):
   pygame.draw.circle(screen, (100, 100, 100), [x, y], 10) 
   
theta = 0
running = True
d = 0
while running:
    d = math.sqrt((ObjectX - particleX)**2 + (ObjectY - particleY)**2)
    
    theta += 0.0001
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    particle(particleX, particleY, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
  #  particle(400, 300, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
    particle(particleX*12, particleY*1.4, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*1.3, particleY, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*1.1+10, particleY+100, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX, particleY*0.7, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*0.8, particleY*1.4, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX, particleY*1.2, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*1.3+10, particleY+100, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*1.21, particleY*0.9, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*10+2, particleY*1.4, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*0.7+30, particleY, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*0.9+60, particleY+100, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    particle(particleX*1.35, particleY*0.7, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 5)
    #particle(400, 300, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
    Object(ObjectX, ObjectY)

    particleX = (400) + math.cos(theta*d+.01) * (150)
    particleY = (300) - math.sin(theta*d+.02)* (150)

    print(particleX, particleY)
    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()
