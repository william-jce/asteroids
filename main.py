import sys
import pygame
from constants import *
from player import Player
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        updatable.update(dt)
        
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
