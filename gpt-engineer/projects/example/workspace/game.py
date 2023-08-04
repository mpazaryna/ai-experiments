from snake import Snake
from food import Food
from controller import Controller
from view import View

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.controller = Controller(self.snake)
        self.view = View(self.snake, self.food)

    def run(self):
        while True:
            self.controller.handle_input()
            self.snake.move()
            if self.snake.check_collision():
                break
            if self.snake.eat(self.food):
                self.food.place()
            self.view.render()
