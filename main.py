import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     return
                
        screen.fill(color=(0, 0, 0))

        updatable.update(dt)

        for item in drawable:
             item.draw(screen)

        for object in asteroids:
             if player.collisioncheck(object):
                  print("Game Over!")
                  sys.exit()


        # updates screen change
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
