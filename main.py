# main.py (outside ping_pong folder)
import pygame
from ping_pong.game import Game
from ping_pong.settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping Pong Game")

    game = Game(screen)

    # Example: change ball speed after each loss
    speeds = [(6, 4), (7, 5), (8, 6)]
    speed_index = 0

    running = True
    while running:
        keys = pygame.key.get_pressed()

        # Control paddles
        if keys[pygame.K_w]:
            game.control_paddle1(up=True)
        if keys[pygame.K_s]:
            game.control_paddle1(up=False)
        if keys[pygame.K_UP]:
            game.control_paddle2(up=True)
        if keys[pygame.K_DOWN]:
            game.control_paddle2(up=False)

        # Check if ball scored and update speed
        prev_score = (game.score1, game.score2)
        running = game.tick()
        new_score = (game.score1, game.score2)
        if new_score != prev_score:
            # change speed for next serve
            speed_index = (speed_index + 1) % len(speeds)
            game.set_ball_speed(*speeds[speed_index])

    pygame.quit()

if __name__ == "__main__":
    main()
