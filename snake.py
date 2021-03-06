class Snake:

    def __init__(self, heading, head_pos, *body_pos):
        self.head = head_pos #tuple of cordinates containing the position of the head
        self.body = [x for x in body_pos] #list of tuples containing the positions of the body pieces
        self.heading = heading #string containing the direction of the snake in form of a letter (N, S, E, W)
        self.length = len(self.body) + 1 #length of the snake
    
    def move(self, food_pos):
        self.body.insert(0, self.head)
        match self.heading:
            case 'N': 
                self.head = (self.head[0], self.head[1] - 1)
            case 'S':
                self.head = (self.head[0], self.head[1] + 1)
            case 'E':
                self.head = (self.head[0] + 1, self.head[1])
            case 'W':
                self.head = (self.head[0] - 1, self.head[1])
        if not self.head == food_pos:
            self.body.pop(-1)
            if self.head in self.body or self.head[0] < 0 or self.head[0] > 19 or self.head[1] < 0 or self.head[1] > 19:
                return "H"
            return 'N'
        return 'A'
    
    def turn(self, direction):
        if self.heading == direction:
            return
        match direction:
            case 'N': 
                if self.heading == 'S':
                    return
                self.heading = 'N'
            case 'S':
                if self.heading == 'N':
                    return
                self.heading = 'S'
            case 'E':
                if self.heading == 'W':
                    return
                self.heading = 'E'
            case 'W':
                if self.heading == 'E':
                    return
                self.heading = 'W'