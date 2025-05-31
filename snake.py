import pygame
from settings import GRID_SIZE, GREEN, DARK_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    """Represents the snake in the game."""
    def __init__(self):
        """Initializes the snake with a default size and direction."""
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.growing = False
        
        self.directions = [(1, 0), (1, 0), (1, 0)]
        
        scale_factor = 4
        image_size = int(GRID_SIZE * scale_factor)
        
        self.segment_image = pygame.image.load("assets/rand.png").convert_alpha()
        self.segment_image = pygame.transform.scale(self.segment_image, (image_size, image_size))

        self.image_offset = (image_size - GRID_SIZE) // 2

        self.grow_sound = pygame.mixer.Sound("assets/Birl.mp3")

    def move(self):
        """Moves the snake in the current direction and grows if necessary."""
        head_x, head_y = self.body[0]
        delta_x, delta_y = self.direction
        new_head = (head_x + delta_x, head_y + delta_y)
        
        self.body.insert(0, new_head)
        self.directions.insert(0, self.direction)
        
        if not self.growing:
            self.body.pop()
            self.directions.pop()
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
        self.grow_sound.play()

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
        for i, (segment, direction) in enumerate(zip(self.body, self.directions)):
            x, y = segment
            draw_x = x * GRID_SIZE - self.image_offset
            draw_y = y * GRID_SIZE - self.image_offset

            # Determina o ângulo com base na direção
            angle = 0
            if direction == (1, 0):   
                angle = 270
            elif direction == (-1, 0):  
                angle = 90
            elif direction == (0, -1):  
                angle = 0
            elif direction == (0, 1):   
                angle = 180

            rotated_image = pygame.transform.rotate(self.segment_image, angle)
            surface.blit(rotated_image, (draw_x, draw_y))

