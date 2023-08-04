import pygame

class Controller:
    def __init__(self, snake):
        self.snake = snake

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    self.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = (1, 0)
