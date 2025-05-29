import pygame
import random
from settings import GRID_SIZE, RED, SCREEN_WIDTH, SCREEN_HEIGHT

class Food:
    """Represents the food in the game."""

    def __init__(self, snake_body):
        """
        Initializes the food in a random position not occupied by the snake.

        Args:
            snake_body (list): List of coordinates occupied by the snake.
        """
        self.position = self._generate_position(snake_body)

    def _generate_position(self, snake_body):
        """
        Generates a valid random position for the food.

        Args:
            snake_body (list): Coordinates occupied by the snake.

        Returns:
            tuple: (x, y) position of the food.
        """
        while True:
            pos = (
                random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1),
                random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1)
            )
            if pos not in snake_body:
                return pos

    def draw(self, surface):
        """
        Draws the food on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the food on.
        """
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)
