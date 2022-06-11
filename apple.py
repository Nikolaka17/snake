from random import randint

class Apple:
    def __init__(self):
        self.apple_pos = (10,10)
        self.move_apple([(10,10), (10,11), (10,12)])
    
    def move_apple(self, snake_pieces):
        while True:
            x = randint(0, 19)
            y = randint(0, 19)
            if (x, y) not in snake_pieces:
                self.apple_pos = (x, y)
                break