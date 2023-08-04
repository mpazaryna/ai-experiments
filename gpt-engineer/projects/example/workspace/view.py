import pygame

class View:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def render(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(segment[0]*20, segment[1]*20, 20, 20))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0]*20, self.food.position[1]*20, 20, 20))
        pygame.display.flip()
