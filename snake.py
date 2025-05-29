import pygame
from settings import GRID_SIZE, GREEN, DARK_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    """Represents the snake in the game."""

    def __init__(self):
        """Initializes the snake with a default size and direction."""
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.growing = False

    def move(self):
        """Moves the snake in the current direction and grows if necessary."""
        head_x, head_y = self.body[0]
        delta_x, delta_y = self.direction
        new_head = (head_x + delta_x, head_y + delta_y)
        self.body.insert(0, new_head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def change_direction(self, new_direction):
        """
        Changes the direction of the snake, avoiding direct reversal.

        Args:
            new_direction (tuple): The new direction (dx, dy).
        """
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow(self):
        """Marks the snake to grow in the next move."""
        self.growing = True

    def collided(self):
        """
        Checks if the snake collided with itself or the walls.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] < 0 or head[1] < 0 or
            head[0] >= SCREEN_WIDTH // GRID_SIZE or
            head[1] >= SCREEN_HEIGHT // GRID_SIZE
        )

    def draw(self, surface):
        """
        Draws the snake on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the snake on.
        """
        for segment in self.body:
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GREEN, rect)
            pygame.draw.rect(surface, DARK_GREEN, rect, 1)
