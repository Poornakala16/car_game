import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
speed = 5

# Player car
car_width = 50
car_height = 60

# Enemy car
enemy_width = 50
enemy_height = 60

font = pygame.font.SysFont(None, 45)


def message_display(text, color):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(width / 2, height / 2))
    win.blit(text_surf, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)


def game_loop():
    car_x = width * 0.45
    car_y = height * 0.8
    car_speed = 0

    enemy_x = random.randint(0, width - enemy_width)
    enemy_y = -enemy_height
    enemy_speed = speed

    score = 0
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_speed = -5
                elif event.key == pygame.K_RIGHT:
                    car_speed = 5

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    car_speed = 0

        car_x += car_speed

        win.fill(white)

        # Draw enemy
        pygame.draw.rect(win, red, (enemy_x, enemy_y, enemy_width, enemy_height))
        enemy_y += enemy_speed

        # Draw player car
        pygame.draw.rect(win, blue, (car_x, car_y, car_width, car_height))

        # Score
        score_text = font.render(f"Score: {score}", True, black)
        win.blit(score_text, (10, 10))

        # Boundaries
        if car_x < 0 or car_x > width - car_width:
            message_display("You Crashed!", red)
            return

        # Collision
        if car_y < enemy_y + enemy_height and car_y + car_height > enemy_y:
            if car_x < enemy_x + enemy_width and car_x + car_width > enemy_x:
                message_display("You Crashed!", red)
                return

        # Enemy respawn and score increment
        if enemy_y > height:
            enemy_y = -enemy_height
            enemy_x = random.randint(0, width - enemy_width)
            score += 1
            enemy_speed += 0.2  # Increase speed slightly

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


game_loop()

