import random

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.place()

    def place(self):
        self.position = (random.randint(0, 10), random.randint(0, 10))
