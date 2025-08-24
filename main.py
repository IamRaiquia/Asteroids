import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     return
                
        screen.fill(color=(0, 0, 0))

        updatable.update(dt)

        for item in drawable:
             item.draw(screen)

        for asteroid in asteroids:
             if player.collisioncheck(asteroid):
                  print("Game Over!")
                  sys.exit()

        for asteroid in asteroids:
             for shot in shots:
                  if asteroid.collisioncheck(shot):
                       shot.kill()
                       asteroid.split()
                       break

        # updates screen change
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
