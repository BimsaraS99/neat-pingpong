# game.py
import pygame
from .paddle import Paddle
from .ball import Ball
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FPS

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)

        # Paddles
        self.paddle1 = Paddle(20, SCREEN_HEIGHT // 2 - 50)
        self.paddle2 = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - 50)

        # Ball
        self.ball = Ball()

        # Scores
        self.score1 = 0
        self.score2 = 0

        # Default ball speed (can be changed externally)
        self.next_ball_speed = (self.ball.speed_x, self.ball.speed_y)

    # --- External control methods ---
    def control_paddle1(self, up: bool):
        if up:
            self.paddle1.move_up()
        else:
            self.paddle1.move_down()

    def control_paddle2(self, up: bool):
        if up:
            self.paddle2.move_up()
        else:
            self.paddle2.move_down()

    def set_ball_speed(self, x, y):
        """Set speed for next serve/reset."""
        self.next_ball_speed = (x, y)
        self.ball.set_speed(x, y)

    # --- Game loop internals ---
    def update(self):
        scorer = self.ball.move(self.paddle1, self.paddle2)
        if scorer == "left":
            self.score1 += 1
            self.ball.reset(*self.next_ball_speed)
        elif scorer == "right":
            self.score2 += 1
            self.ball.reset(*self.next_ball_speed)

    def draw(self):
        self.screen.fill(BLACK)
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)

        # Center line
        pygame.draw.aaline(self.screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        # Scores
        score_text = self.font.render(f"{self.score1}   {self.score2}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

        pygame.display.flip()

    def tick(self):
        """Advance one frame and return running state."""
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.update()
        self.draw()
        return True
