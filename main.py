import pygame
from sys import exit
from snake import Snake

class Window:
    def __init__(self, width, height):
        #general setup
        self.player = Snake("N", (10, 10), (10, 11), (10, 12))
        self.width = width
        self.height = height
        self.block_size = 20

        #pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.fps = 60
    
    def update_screen(self):
        for x in range(self.width):
            for y in range(self.height):
                color = (200, 200, 200)
                if (x, y) in self.player.body or (x, y) == self.player.head:
                    color = (0, 200, 0)
                rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, color, rect, 1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    pass
            
            self.update_screen()
            pygame.display.update()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    game = Window(400, 400)
    game.run()