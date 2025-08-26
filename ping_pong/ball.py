# ball.py
import pygame
import random
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SIZE, WHITE

class Ball:
    def __init__(self, speed_x=5, speed_y=5):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2,
                                SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
                                BALL_SIZE, BALL_SIZE)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def reset(self, speed_x=None, speed_y=None):
        """Reset ball position and optionally set a new speed, with random direction."""
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        if speed_x is not None:
            self.speed_x = speed_x
        if speed_y is not None:
            self.speed_y = speed_y

        # Randomize direction on each reset
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))

    def set_speed(self, x, y):
        """Externally control ball speed."""
        self.speed_x = x
        self.speed_y = y

    def move(self, paddle1, paddle2):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

        # Bounce paddles
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.speed_x *= -1

        # Scoring
        if self.rect.left <= 0:
            return "right"
        elif self.rect.right >= SCREEN_WIDTH:
            return "left"
        return None

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)
