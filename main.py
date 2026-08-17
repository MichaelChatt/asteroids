from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
