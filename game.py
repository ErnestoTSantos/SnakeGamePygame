import pygame
import sys
from snake import Snake
from food import Food
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS,
    UP, DOWN, LEFT, RIGHT, WHITE
)

from settings import BROWN_DARK, BROWN_LIGHT, GREEN



class Game:
    """Main class responsible for running the Snake game."""

    def __init__(self):
        """Initializes the game window, snake, food, and clock."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game 🐍")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        self.start_font = pygame.font.SysFont(None, 36)
        self._reset()
        self.started = False

    def _reset(self):
        """Resets the game state to the beginning."""
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.running = False
        self.game_over = False

    def run(self):
        """Main game loop."""
        while True:
            self._handle_events()

            if self.running:
                self.snake.move()

                if self.snake.body[0] == self.food.position:
                    self.snake.grow()
                    self.food = Food(self.snake.body)

                if self.snake.collided():
                    self._trigger_game_over()

            self._render()
            self.clock.tick(FPS)

    def _handle_events(self):
        """Handles keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if not self.started:
                    self.started = True
                    self.running = True
                elif self.running:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.change_direction(RIGHT)
                elif self.game_over:
                    if event.key == pygame.K_r:
                        self._reset()
                        self.started = True
                        self.running = True

    def _render(self):
        """Renders all game elements on the screen."""
        self._draw_dynamic_background()

        if not self.started:
            self._draw_start_screen()
        else:
            self.snake.draw(self.screen)
            self.food.draw(self.screen)

            if self.game_over:
                self._draw_game_over()

        pygame.display.flip()

    def _trigger_game_over(self):
        """Triggers the game over state."""
        self.running = False
        self.game_over = True

    def _draw_game_over(self):
        """Draws the Game Over message and restart instructions."""
        game_over_text = self.font.render("Game Over", True, WHITE)
        restart_text = pygame.font.SysFont(None, 32).render("Press R to restart", True, WHITE)

        rect1 = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        rect2 = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))

        self.screen.blit(game_over_text, rect1)
        self.screen.blit(restart_text, rect2)

    def _draw_start_screen(self):
        """Draws the start screen message."""
        text = self.start_font.render("Press any key to start", True, WHITE)
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, rect)

    def _draw_dynamic_background(self):
        """Draws a static brown checkerboard with green borders."""
        cell_size = 80  # maior pra destacar
        for x in range(0, SCREEN_WIDTH, cell_size):
            for y in range(0, SCREEN_HEIGHT, cell_size):
                if (x // cell_size + y // cell_size) % 2 == 0:
                    color = BROWN_LIGHT
                else:
                    color = BROWN_DARK

                pygame.draw.rect(self.screen, color, (x, y, cell_size, cell_size))

                pygame.draw.rect(self.screen, GREEN, (x, y, cell_size, cell_size), 2)
