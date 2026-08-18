from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import pygame
import sys
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 )
    asteroidfield = AsteroidField()
    while True == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for rocks in asteroids:
            if rocks.collides_with(player):
                log_event("player_hit")
                print("Game Over")
                sys.exit()
            for bullets in shots():
                if rocks.collides_with(bullets):
                    bullets.kill()
                    rocks.kill()
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
