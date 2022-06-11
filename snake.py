class Snake:

    def __init__(self, heading, head_pos, *body_pos):
        self.head = head_pos #tuple of cordinates containing the position of the head
        self.body = [x for x in body_pos] #list of tuples containing the positions of the body pieces
        self.heading = heading #string containing the direction of the snake in form of a letter (N, S, E, W)
    
    def move(self, ate_food):
        self.body.insert(0, self.head)
        if not ate_food:
            self.body.pop(-1)
        match self.heading:
            case 'N': 
                self.head = (self.head[0], self.head[1] - 1)
            case 'S':
                self.head = (self.head[0], self.head[1] + 1)
            case 'E':
                self.head = (self.head[0] + 1, self.head[1])
            case 'W':
                self.head = (self.head[0] - 1, self.head[1])
    
    def turn(self, direction):
        if self.heading == direction:
            return
        match direction:
            case 'N': 
                self.heading = 'N'
            case 'S':
                self.heading = 'S'
            case 'E':
                self.heading = 'E'
            case 'W':
                self.heading = 'W'