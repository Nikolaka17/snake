import pygame
from sys import exit
from snake import Snake

class Window:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = 60
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    game = Window(1280, 720)
    game.run()