class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = (0, 1)

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        return self.body[0] in self.body[1:]

    def eat(self, food):
        if self.body[0] == food.position:
            self.grow()
            return True
        return False
